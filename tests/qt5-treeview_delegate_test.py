#!/usr/bin/env python2
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"




import sys
import os
import zmq
import uuid
import setproctitle
import multiprocessing
import subprocess
import time
import glob

# sys.path.append(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1]))
progPath = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
rbhusPath = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2])
sys.path.append(rbhusPath)
import rbhus.debug
import rbhus.constantsPipe
import rbhus.utilsPipe
import rbhus.dfl

main_ui_file = os.path.join(rbhusPath, "rbhusUI", "lib", "qt5", "folderManager", "main_listView.ui")
mediaThumbz_ui_file = os.path.join(rbhusPath, "rbhusUI", "lib", "qt5", "folderManager", "mediaThumbz.ui")
rbhus.debug.info(main_ui_file)


import os
import simplejson
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QFileIconProvider, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, uic, QtGui, QtWidgets



assPath = sys.argv[1]
ROOTDIR = rbhus.utilsPipe.getAbsPath(sys.argv[1])
CUR_ROOTDIR_POINTER = os.path.join(ROOTDIR,"-")
COMPOUND_PATHS = rbhus.utilsPipe.getCompoundPaths(assPath)
print(COMPOUND_PATHS)

fileDetsDict = {}
fileIconThreadRunning = None
fileThumbzWidget = {}

context = zmq.Context()

def jsonWrite(jFile, jData):
  try:
    fJsonFD = open(jFile, "w")
    simplejson.dump(jData, fJsonFD)
    fJsonFD.flush()
    fJsonFD.close()
    return (1)
  except:
    return (0)


def jsonRead(jFile):
  try:
    fJsonFD = open(jFile, "r")
    fThumbzDetails = simplejson.load(fJsonFD)
    fJsonFD.close()
    return (fThumbzDetails)
  except:
    return (0)


class QListWidgetItemSort(QListWidgetItem):


  def __lt__(self, other):
    return self.data(QtCore.Qt.UserRole) < other.data(QtCore.Qt.UserRole)

  def __ge__(self, other):
    return self.data(QtCore.Qt.UserRole) > other.data(QtCore.Qt.UserRole)



class getIconDoneEvent(QtCore.QThread):
  iconGenerated = QtCore.pyqtSignal(object)
  def __init__(self,iconQDoneSignal, parent=None):
    super(getIconDoneEvent,self).__init__(parent)
    self.iconQDoneSignal = iconQDoneSignal


  def run(self):
    while True:
      iconObj = self.iconQDoneSignal.get()
      # print('received python object:', iconObj.mainFile)
      try:
        self.iconGenerated.emit(iconObj)
      except:
        pass






class server(QtCore.QThread):
  def __init__(self,iconQDoneSignal,parent=None):
    super(server,self).__init__(parent)
    self.iconQDoneSignal = iconQDoneSignal
    self._context = zmq.Context()
    self._portServer = 55555
    self._portWorker = 55999

  def process(self, iconQ, iconQDoneSignal):
    setproctitle.setproctitle("server-worker-process")


    while(True):
      fileDets = iconQ.get()
      rbhus.debug.info(fileDets)
      fAbsPath = fileDets.absPath
      mimeType = fileDets.mimeType
      fLockPath = rbhus.dfl.LockFile(fAbsPath,timeout=0,expiry=30)
      fDir = os.path.dirname(fAbsPath)
      fName = os.path.basename(fAbsPath)
      fThumbzDbDir = os.path.join(fDir, ".thumbz.db")
      try:
        os.mkdir(fThumbzDbDir)
      except:
        pass
      fJson = os.path.join(fThumbzDbDir,fName + ".json")
      fThumbz = os.path.join(fThumbzDbDir,fName + ".png")
      fModifiedTime = os.path.getmtime(fAbsPath)
      # if (os.path.exists(fLockPath.lock_file)):
      #   if ((time.time() - os.path.getmtime(fLockPath.lock_file)) > 60):
      #     rbhus.debug.info("locked file for more than 1 minute : " + str(fAbsPath))

      if (os.path.exists(fThumbzDbDir)):

        if (os.path.exists(fJson)):
          try:
            with fLockPath:
              fThumbzDetails = jsonRead(fJson)
              if (fThumbzDetails[fName] < fModifiedTime):
                try:
                  thumbzCmd = rbhus.constantsPipe.mimeConvertCmds[mimeType].format(fAbsPath, fThumbz)
                except:
                  thumbzCmd = None
                if (thumbzCmd):
                  rbhus.debug.info(thumbzCmd)
                  p = subprocess.Popen(thumbzCmd, shell=True)
                  retcode = p.wait()
                  print("generated thumb : "+ str(fThumbz))
                  # while(retcode == None):
                  #   retcode = p.poll()
                  #   time.sleep(0.01)

                  if (retcode == 0):
                    fThumbzDetails = {fName: fModifiedTime}
                    jsonWrite(fJson, fThumbzDetails)
          except:
            rbhus.debug.info("file is updated by someone : " + str(fAbsPath))
        else:
          fThumbzDetails = {fName: fModifiedTime}
          jsonWrite(fJson, fThumbzDetails)
          try:
            thumbzCmd = rbhus.constantsPipe.mimeConvertCmds[mimeType].format(fAbsPath, fThumbz)
          except:
            thumbzCmd = None
          if (thumbzCmd):
            rbhus.debug.info(thumbzCmd)
            p = subprocess.Popen(thumbzCmd, shell=True)
            retcode = p.wait()

      fileDets.thumbFile = fThumbz
      fileDets.mainFile = fAbsPath
      fileDets.subPath = fDir
      iconQDoneSignal.put(fileDets)






  def _worker(self,worker_url,iconQ):

    worker_id = uuid.uuid4()
    setproctitle.setproctitle("server-worker : "+ str(worker_id))
    rbhus.debug.info("running worker")
    rbhus.debug.info (worker_url +" : "+ str(worker_id))
    context = zmq.Context()
    # Socket to talk to dispatcher
    socket = context.socket(zmq.REP)
    socket.poll(timeout=1)
    socket.connect(worker_url)


    while True:
      fileDets = socket.recv_pyobj()
      # setproctitle.setproctitle("server-worker : " + str(fileDets.absPath))
      socket.send_pyobj(fileDets)
      rbhus.debug.info("Filepath recieved : [ {0} ]".format(str(fileDets.absPath)))
      iconQ.put(fileDets)

  def run(self):
    rbhus.debug.info("server run")
    pool_size = 4
    worker_port = self._portWorker
    server_port = self._portServer
    url_worker = "tcp://127.0.0.1:{0}".format(worker_port)
    url_client = "tcp://*:{0}".format(server_port)
    clients = self._context.socket(zmq.ROUTER)
    try:
      clients.bind(url_client)
    except:
      rbhus.debug.info (sys.exc_info())
      self._context.term()
      sys.exit(1)

    # Socket to talk to workers
    workers = self._context.socket(zmq.DEALER)
    try:
      workers.bind(url_worker)
    except:
      rbhus.debug.info (sys.exc_info())
      self._context.term()
      sys.exit(1)


    iconQ = multiprocessing.Queue(pool_size)

    multiprocessing.Pool(processes=pool_size, initializer=self.process, initargs = (iconQ,self.iconQDoneSignal))
    # Launch pool of worker process
    multiprocessing.Pool(processes=pool_size, initializer=self._worker, initargs=(url_worker,iconQ, ))
    # p.daemon = False

    zmq.proxy(clients, workers)

    print("We never get here but clean up anyhow")
    try:
      clients.close()
      workers.close()
      self._context.term()
    except:
      print(sys.exc_info())
    self.finished.emit()


class fileDirLoadedThread(QtCore.QThread):
  fileIcon = QtCore.pyqtSignal(object)
  iconProcessStarted = QtCore.pyqtSignal()
  def __init__(self, filesLoaded,pathSelected):
    super(fileDirLoadedThread, self).__init__()
    self._ip = 'localhost'
    self._port = 55555
    self.filesLoaded = filesLoaded
    self._pleaseStop = False
    self.pathSelected = pathSelected
    global context
    self.socket = context.socket(zmq.REQ)
    self.socket.connect("tcp://{0}:{1}".format("localhost", "55555"))
    # rbhus.debug.info("Sending request {0} ".format(fileDets))


  def pleaseStop(self):
    self._pleaseStop = True

  def run(self):
    for filePath in self.filesLoaded:
      if(self._pleaseStop):
        break
      if(os.path.isfile(filePath)):
        for mimeType in rbhus.constantsPipe.mimeTypes.keys():
          if (self._pleaseStop):
            break
          mimeExts = rbhus.constantsPipe.mimeTypes[mimeType]
          for mimeExt in mimeExts:
            if (self._pleaseStop):
              break


            if (filePath.endswith(mimeExt)):

              fSubPath = self.pathSelected

              if (not fSubPath):
                fSubPath = "-"


              fileDets = rbhus.utilsPipe.thumbz_db()
              fileDets.mainFile = filePath
              fileDets.absPath = filePath
              fileDets.subPath = fSubPath
              fileDets.mimeType = mimeType
              fileDets.mimeExt = mimeExt
              fAbsPath = fileDets.absPath
              fDir = os.path.dirname(fAbsPath)
              fName = os.path.basename(fAbsPath)
              fThumbzDbDir = os.path.join(fDir, ".thumbz.db")
              fThumbz = os.path.join(fThumbzDbDir, fName + ".png")
              fileDets.thumbFile = fThumbz

              try:
                self.fileIcon.emit(fileDets)
                self.startIconGen(fileDets)
              except:
                print(sys.exc_info())
              time.sleep(0.01)
    self.socket.close()
    self.finished.emit()

  def startIconGen(self,fileDets):



    self.socket.send_pyobj(fileDets)
    # rbhus.debug.info("sending filepath")
    recvd_obj = self.socket.recv_pyobj()



class FSM(QFileSystemModel):

  def __init__(self,**kwargs):
    super(FSM, self).__init__(**kwargs)
    self.fileDets = None



  def canFetchMore(self,idx):
    if (self.filePath(idx) == CUR_ROOTDIR_POINTER):
      rootIdx = self.index(ROOTDIR)
      return super(FSM, self).fetchMore(idx)
    elif (self.filePath(idx).endswith(".thumbz.db")):
      return False
    else:
      return super(FSM, self).canFetchMore(idx)

  # def rowCount(self,idx):
  #   rbhus.debug.info(idx.row())
  #   # return(idx.row() + 1)
  #   return super(FSM, self).rowCount(idx)

  def fetchMore(self,idx):
    if (self.filePath(idx) == CUR_ROOTDIR_POINTER):
      rootIdx = self.index(ROOTDIR)
      return super(FSM, self).fetchMore(idx)
    elif(self.filePath(idx).endswith(".thumbz.db")):
      return None
    else:
      return super(FSM, self).fetchMore(idx)

  def headerData(self,section,orientation,role):
    if(section == 0 and role == QtCore.Qt.DisplayRole):
      return "Folders"
    else:
      return super(FSM, self).headerData(section,orientation,role)

  def filePath(self, idx):
    rootIdx = self.index(CUR_ROOTDIR_POINTER)
    if(idx == rootIdx):
      return ROOTDIR
    else:
      return super(FSM, self).filePath(idx)



def dirSelected(idx, modelDirs, main_ui):
  global fileThumbzWidget
  global fileIconThreadRunning


  pathSelected = modelDirs.filePath(idx)
  print(pathSelected)
  if(fileIconThreadRunning):
    try:
      fileIconThreadRunning.disconnect()
      fileIconThreadRunning.pleaseStop()
      fileIconThreadRunning.wait()
      fileIconThreadRunning = None
    except:
      pass


  fileThumbz.clear()
  # main_ui.listFiles.clear()






  if(pathSelected == CUR_ROOTDIR_POINTER):

    fileGlob = glob.glob(ROOTDIR + os.sep + "*")
  else:
    fileGlob = glob.glob(pathSelected + os.sep + "*")
  try:
    fileGlob.remove("-")
  except:
    pass
  if(fileGlob):
    fileGlob.sort()
    fileIconThreadRunning = fileDirLoadedThread(fileGlob,pathSelected)
    fileIconThreadRunning.fileIcon.connect(lambda fileIconDets, pathSelected = pathSelected, main_ui=main_ui :fileIconActivate(fileIconDets,pathSelected,main_ui))
    fileIconThreadRunning.start()





def fileIconActivate(fileIconDets,pathSelected, main_ui):
  # print("recvd preview : "+ str(fileIconDets.subPath))
  global fileThumbzWidget
  itemWidget = uic.loadUi(mediaThumbz_ui_file)
  itemWidget.labelImageName.setText(os.path.basename(fileIconDets.mainFile))

  try:
    modifiedT = os.path.getmtime(fileIconDets.mainFile)
  except:
    modifiedT = 0
  # print(time.ctime(modifiedT))
  itemWidget.groupBoxThumbz.setToolTip("subdir: " + fileIconDets.subPath + "\nmodified : " + str(time.ctime(modifiedT)))
  # itemWidget.pushButtonImage.clicked.connect(lambda x, imagePath=fileIconDets.mainFile, mimeType=fileIconDets.mimeType: imageWidgetClicked(imagePath, mimeType=mimeType))

  item = QListWidgetItemSort()
  icon = QtGui.QIcon(rbhus.constantsPipe.mimeLogos[fileIconDets.mimeType])
  # icon = fileIconProvider()
  # icon = QtGui.QIcon(rbhus.constantsPipe.mimeLogos[fileIconDets.mimeType])
  itemWidget.pushButtonLogo.setIcon(icon)
  # item.setSizeHint(QtCore.QSize(96,96))
  item.setData(QtCore.Qt.UserRole, os.path.basename(fileIconDets.mainFile))
  item.setToolTip(fileIconDets.subPath + os.sep + os.path.basename(fileIconDets.mainFile))
  item.media = fileIconDets
  item.setSizeHint(itemWidget.sizeHint() + QtCore.QSize(10, 10))
  main_ui.listFiles.addItem(item)
  main_ui.listFiles.setItemWidget(item, itemWidget)
  fileThumbz[fileIconDets.mainFile] = itemWidget
  # print("thumbz added :: "+ fileIconDets.mainFile)



def imageWidgetClicked(imagePath,mimeType=None):
  if(mimeType):
    if(mimeType != "blender"):
      import webbrowser
      webbrowser.open(imagePath)
  else:
    import webbrowser
    webbrowser.open(imagePath)

def imageWidgetUpdated(fileDets):
  global fileThumbzWidget
  # print("updated icon : "+ fileDets.mainFile)
  try:

    fileThumbz[fileDets.mainFile].pushButtonImage.setIcon(QtGui.QIcon(fileDets.thumbFile))
    fileThumbz[fileDets.mainFile].pushButtonImage.setIconSize(QtCore.QSize(92,92))
    return
  except:
    print("wtf :: "+ str(sys.exc_info()))


def filesSelected(modelFiles, main_ui):
  selectedIdx = main_ui.listFiles.selectedIndexes()
  rbhus.debug.info(selectedIdx)
  for idx in selectedIdx:
    print("--------")
    print(modelFiles.filePath(idx))


def mainGui(main_ui):
  iconQDoneSignal = multiprocessing.Queue(1)
  iconServer = server(iconQDoneSignal=iconQDoneSignal,parent=main_ui)
  iconServer.start()
  main_ui.setWindowTitle("Ass Folds")
  main_ui.splitter.setStretchFactor(1,10)



  modelDirs = FSM()
  modelDirs.setFilter( QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)
  modelDirs.setRootPath(ROOTDIR)
  filterList = COMPOUND_PATHS
  # modelDirs.setNameFilters(filterList)
  # modelDirs.setNameFilterDisables(False)


  modelFiles = FSM()
  modelFiles.setFilter( QtCore.QDir.Files | QtCore.QDir.NoDotAndDotDot)
  modelFiles.setRootPath(ROOTDIR)



  main_ui.treeDirs.setModel(modelDirs)



  main_ui.treeDirs.hideColumn(1)
  main_ui.treeDirs.hideColumn(2)
  main_ui.treeDirs.hideColumn(3)

  rootIdx = modelDirs.index(ROOTDIR)
  main_ui.treeDirs.setRootIndex(rootIdx)
  modelDirs.mkdir(rootIdx,"-")
  for x in COMPOUND_PATHS:
    xIdx = modelDirs.index(x)
    main_ui.treeDirs.setRowHidden(xIdx.row(),xIdx.parent(),True)




  curRootIdx = modelDirs.index(CUR_ROOTDIR_POINTER)
  main_ui.treeDirs.setCurrentIndex(curRootIdx)
  # dirSelected(curRootIdx, modelDirs, main_ui)
  iconEventEater = getIconDoneEvent(iconQDoneSignal,parent=main_ui)
  iconEventEater.iconGenerated.connect(imageWidgetUpdated)
  iconEventEater.start()



  main_ui.treeDirs.clicked.connect(lambda idnx, modelDirs=modelDirs, main_ui = main_ui : dirSelected(idnx, modelDirs, main_ui))
  # main_ui.listFiles.clicked.connect(lambda idnx, main_ui = main_ui :filesSelected(modelFiles,main_ui))


  main_ui.show()
  main_ui.update()





if __name__ == '__main__':
  app = QApplication(sys.argv)
  main_ui = uic.loadUi(main_ui_file)
  mainGui(main_ui)
  # ex = App()
  sys.exit(app.exec_())