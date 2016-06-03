# -*- coding : utf-8 -*-

import cv2
import numpy as np

def process(image, WD, HG):
    """一次性预处理
    @param image 待处理图像
    @param WD 归一化宽度
    @param HG 归一化高度
    
    @return img 处理后的图像
    """
    # 第一步：如果是rgb图像，则转化为灰度图像
    imgGray = rgb2gray(image)
    # 第二步：将灰度图二值化
    img = gray2whiteblack(imgGray)
    # 第三步：梯度锐化
    
    
    return img
    
def rgb2gray(image):
    """将RGB图像转化为灰度图
    @param image 输入的np.array
    
    @return img 输出的灰度图像
    """
    if image.ndim == 3:#判断通道数
        img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        img = image
    return img

def gray2whiteblack(image):
    """使用Otsu自适应滤波，将灰度图转化为二值图像
    @param image 输入的灰度图像
    
    @return img 二值图像
    """
    retVal, img = cv2.threshold(image,200,255,cv2.THRESH_OTSU)
    return img

