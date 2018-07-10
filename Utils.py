# coding=utf-8
import time
import os
import re
def isPng(path):
    return str(path).endswith('.png') or  str(path).endswith('.PNG')

def isVideo(path):
    return str(path).endswith('.mp4')

def isAllowConvert2Time(path):
    return isPng(path) or isVideo(path)

def fileName(path):
    return os.path.basename(path)

def extractTimeFromFile(path):
    name = fileName(path)
    return extractTime(name)

def extractTime(content):
    timestr = ''
    timeformat = ''
    patterns = [r'(\d{8}[-]\d{6})', r'(\d{8}[_]\d{6})', r'(\d{4}-\d{1,2}-\d{2}\s\d{2}:\d{2}:\d{2})', r'(\d{4}/\d{1,2}/\d{2}\s\d{2}:\d{2}:\d{2})']
    formats = ['%Y%m%d-%H%M%S', '%Y%m%d_%H%M%S', '%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S']
    pf = zip(patterns, formats)
    for (p, f) in pf:
        mat = re.search(p, content)
        if mat:
            timestr = mat.group()
            timeformat = f
            break

    if timestr and timeformat:
        timeArray = time.strptime(timestr, timeformat)
        timestamp = time.mktime(timeArray)  # 转出来的单位是秒
        print(timestamp)
        return timestamp
    else:
        return -1


    # 把秒时间戳转字符串时间
def convertSeconds2TimeStr(timestamp):
    times = time.localtime(timestamp)
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", times)
    return timestr