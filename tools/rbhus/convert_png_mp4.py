#!/usr/bin/python

import multiprocessing
import sys
import glob
import subprocess
import os


path = sys.argv[1]
cpus = multiprocessing.cpu_count()
print(cpus)
print(path)

pngs = glob.glob(path.rstrip(os.sep) + os.sep +"*.png")
png = "_".join(pngs[-1].split(".")[0].split("_")[:-1]) +"_%04d.png"
flv = path.rstrip(os.sep) + os.sep +"video.mp4"
ffmpeg = "yes | ffmpeg -i "+ png +" -r 25 -b:v 8000k "+ flv
p = subprocess.Popen(ffmpeg,shell=True)
p.wait()
