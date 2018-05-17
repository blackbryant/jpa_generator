#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os

def getTimeStamp():
    return time.time()

'''
    formate:%Y-%m-%d %H:%M:%S
    2016-03-20 11:45:39形式
'''
def getCurDateTime():
    str=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) 
    return str

'''
    formate:%Y-%m-%d %H:%M:%S
    2016/03/20形式
'''
def getCurDate():
    str=time.strftime("%Y/%m/%d", time.localtime()) 
    return str

def getCurTime():
    str=time.strftime("%H:%M:%S", time.localtime()) 
    return str

def writeFile(dir,fileName, content):
    fullFileName= dir+os.sep+fileName
    mkdirs(dir)
    with open(dir+os.sep+fileName, "w") as file:
        file.write(content)
    return fullFileName

def mkdirs(inputDir):
    if not os.path.isdir(inputDir) : 
       os.makedirs(inputDir)

def dot2Slash(inputDir):
    tempDir = inputDir.replace(".",os.sep)
    return tempDir



