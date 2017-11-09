#!/usr/bin/env python2
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import sys
import os

sys.path.append(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3]))



import multiprocessing
import glob
import subprocess
import uuid
import shutil


path = sys.argv[1]

cpus = multiprocessing.cpu_count()
exrs = glob.glob(path.rstrip(os.sep) + os.sep + "*.exr")
exrs.sort()
mp4 = "_".join(exrs[-1].split(".")[0].split("_")[:-1]) + ".mp4"
exr = "_".join(exrs[-1].split(".")[0].split("_")[:-1]) + "_%04d.exr"
startFrame = exrs[0].split("_")[-1].rstrip(".exr")
endFrame = exrs[-1].split("_")[-1].rstrip(".exr")
inputFileFmt = "_".join(exrs[-1].split(".")[0].split("_")[:-1]) + "_"+ startFrame +"-"+ endFrame +".exr"

ffmpeg = None
if(os.path.exists("/opt/lib/ffmpeg/bin/ffmpeg")):
  ffmpeg = "/opt/lib/ffmpeg/bin/ffmpeg"
else:
  print("Not found : /opt/lib/ffmpeg/bin/ffmpeg")
  ffmpeg = "ffmpeg"

cmd = ffmpeg +" -probesize 50000000 -apply_trc iec61966_2_1 -r 24 -start_number "+ str(startFrame) +" -i "+ exr +" -c:v libx264 -pix_fmt yuv420p -crf 20 -y "+ mp4
# cmd = "djv_convert "+ inputFileFmt +" "+ mp4 +" -default_speed 24 -render_filter_high"
p = subprocess.Popen(cmd,shell=True)
p.wait()
# os.remove(unatron)
