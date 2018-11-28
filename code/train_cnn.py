#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:28:06 2018

@author: guoxiaowen
"""

import numpy as np
import tensorflow as tf
import random
import time
import os
from PIL import Image

#  验证码的保存路径
CAPTCHA_IMAGE_PATH = "/Volumes/study/2018大三上课程/大数据分析/作业/train_picture/"

CAPTCHA_LEN = 4

CHAR_SET_LEN = 10
#    验证码图片的高宽
CAPTCHA_IMAGE_HEIGHT = 60

CAPTCHA_IMAGE_WIDHT =160
#  选取60%作为训练的数据集
TRAIN_IMAGE_PERCENT = 0.6
#   存放训练集的图片名
TRAINING_IMAGE_NAME = []
#   存放验证集的图片名
VALIDATION_IMAGE_NAME = []


#存放训练好的模型的路径
MODEL_SAVE_PATH = '/Volumes/study/2018大三上课程/大数据分析/作业/train_picture/models'


#  获取训练集的图片名
def get_image_file_name(CaptchaImgPath = CAPTCHA_IMAGE_PATH):
    fileName = []
    total = 0
    for filePath in os.listdir(CaptchaImgPath):
        captcha_name = filePath.split('/')[-1]
        fileName.append(captcha_name)
        total += 1
    #  print(fileName)
    return fileName, total

#   get_image_file_name(CAPTCHA_IMAGE_PATH)
    
#将验证码转换为训练时用的标签向量，维数是 40   
#例如，如果验证码是 ‘0296’ ，则对应的标签是
# [1 0 0 0 0 0 0 0 0 0
#  0 0 1 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 1
#  0 0 0 0 0 0 1 0 0 0]
def nameTolabel(name):
    label = np.zeros(CAPTCHA_LEN * CHAR_SET_LEN)
    for i, c in enumerate(name):
        idx = i*CHAR_SET_LEN + ord(c) - ord('0')
        label[idx] = 1
        
 
    return label






