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
    gradient_sharp(img)
    # 第四步：去离散杂点噪声
    remove_scatter_noise(img)
    # 第五步：倾斜度调整
    adjust_slope(img)
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

def gradient_sharp(image):
    """梯度锐化
    @param, return image 输入的图像
    """
    rows, cols = image.shape
    bThre = 2#阈值
    for i in range(rows-1):
        for j in range(cols-1):
            bTemp = abs(int(image[i,j])-int(image[i+1,j]))+ abs(int(image[i,j]) - int(image[i, j+1]))
            if bTemp < 255:
                if bTemp >= bThre:
                    image[i,j] = bTemp
            else:
                image[i,j] = 255
    for j in range(cols):
        image[rows-1, j] = 255
        
def remove_scatter_noise(image):
    """去离散杂点噪声(这个算法效率有点低)
    @param image 输入的二值图像
    
    @return 
    """
    rows, cols = image.shape
    # 设置判断噪声的长度阈值为15
    LEN = 15
    # 将有效点保存到元组
    p = []
    for i in range(rows):
        for j in range(cols):
            if image[i,j] == 0:
                p.append([i,j])
    # 连通搜寻
    while len(p) >0:
        c = [p.pop(0)]
        j = 0
        while j < len(c):
            #遍历当前区域
            t = 0
            for k in range(len(p)):
                if max([abs(p[k-t][0] - c[j][0]), abs(p[k-t][1] - c[j][1])]) <=1:
                    c.append(p.pop(k-t))
                    t = t + 1
            j = j + 1
        if len(c) <=LEN:
            for noise in c:
                image[noise[0], noise[1]] = 255
        
        
def adjust_slope(image):
    pass
