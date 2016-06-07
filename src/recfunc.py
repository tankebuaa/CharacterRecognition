# -*- coding : utf-8 -*-

import cv2
import numpy as np
from numpy import linalg as LA

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
    # 第四步：去离散杂点噪声,并得到分割后的字符区域特征（像素和范围）
    cha = remove_scatter_noise(img)
    # 第五步：归一化调整
    adjust(img, cha, WD, HG)
    return (img, cha)
    
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
    """去离散杂点噪声
    @param image 输入的二值图像
    
    @return 
    """
    # 图片尺寸
    rows, cols = image.shape
    # 设置判断噪声的长度阈值为15
    LEN = 15
    # 标识数组刚开始都是false,没有被访问过
    biaozhi = np.zeros((rows, cols), dtype = np.bool)
    # 字符区域特征字典
    chad = dict()
    # 开始递归访问
    for i in range(rows):
        for j in range(cols):
            # 像素为白点，跳过检测并标记为True
            if image[i,j] == 255:
                biaozhi[i,j] = True
            else:
                # 如果没有被访问过，说明是新的连通区域，则开始递归连通检测
                if biaozhi[i,j] == False:
                    biaozhi[i,j] = True
                    area = [i,i,j,j]#字符区域area = [xmin,xmax,ymin,ymax]
                    con = [(i,j)]# 压入连通区域数组，为第一个点
                    # 锚点，图像，保存锚点的数组
                    detect_connect(i, j, biaozhi, image, rows, cols, con, area)
                    if len(con) < LEN:
                        for noise in con:
                            image[noise[0], noise[1]] = 255
                    else:
                        chad[area[2]] = (con,area)
    # 字符特征列表
    chal = []
    for key in sorted(chad):
        chal.append(chad[key])
    return chal
                    
def detect_connect(i, j, biaozhi, image, rows, cols, con, area):
    """根据锚点，检测连通
    @param i,j 锚点的坐标（图像行和列）
    @param biaozhi 是否已经访问过
    @param image 图像
    @param rows, cols 图像的大小
    @param con 连通区域数组
    @param area 字符连通区域的坐标范围[xmin,xmax,ymin,ymax]
    """
    #右
    if j+1 <cols:
        if biaozhi[i,j+1] == False:
            if image[i,j+1] == 255:
                biaozhi[i,j+1] = True
            else:
                biaozhi[i,j+1] = True
                con.append((i, j+1))
                area[3] = max(area[3],j+1)
                detect_connect(i, j+1, biaozhi, image, rows, cols, con, area)
    #右下
    if i+1<rows and j+1<cols:
        if biaozhi[i+1,j+1] == False:
            if image[i+1,j+1] == 255:
                biaozhi[i+1,j+1] = True
            else:
                biaozhi[i+1,j+1] = True
                con.append((i+1,j+1))
                area[1] = max(area[1], i+1)
                area[3] = max(area[3], j+1)
                detect_connect(i+1, j+1, biaozhi, image, rows, cols, con, area)
    #下
    if i+1 < rows:
        if biaozhi[i+1,j] == False:
            if image[i+1,j] == 255:
                biaozhi[i+1,j] = True
            else:
                biaozhi[i+1,j] = True
                con.append((i+1,j))
                area[1] = max(area[1], i+1)
                detect_connect(i+1, j, biaozhi, image, rows, cols, con, area)
    #左下
    if i+1 <rows and j-1>=0:
        if biaozhi[i+1,j-1] == False:
            if image[i+1,j-1] == 255:
                biaozhi[i+1,j-1] = True
            else:
                biaozhi[i+1,j-1] = True
                con.append((i+1,j-1))
                area[1] = max(area[1], i+1)
                area[2] = min(area[2], j-1)
                detect_connect(i+1, j-1, biaozhi, image, rows, cols, con, area)
    #左
    if j-1>=0:
        if biaozhi[i,j-1] == False:
            if image[i, j-1] == 255:
                biaozhi[i,j-1] = True
            else:
                biaozhi[i,j-1] = True
                con.append((i,j-1))
                area[2] = min(area[2], j-1)
                detect_connect(i, j-1, biaozhi, image, rows, cols, con, area)
    # 左上
    if i-1 >=0 and j-1>=0:
        if biaozhi[i-1,j-1] == False:
            if image[i-1, j-1] == 255:
                biaozhi[i-1,j-1] = True
            else:
                biaozhi[i-1,j-1] = True
                con.append((i-1,j-1))
                area[0] = min(area[0], i-1)
                area[2] = min(area[2], j-1)
                detect_connect(i-1, j-1, biaozhi, image, rows, cols, con, area)
    # 上
    if i-1>=0:
        if biaozhi[i-1,j] == False:
            if image[i-1, j] == 255:
                biaozhi[i-1,j] = True
            else:
                biaozhi[i-1,j] = True
                con.append((i-1,j))
                area[0] = min(area[0], i-1)
                detect_connect(i-1, j, biaozhi, image, rows, cols, con, area)
    # 右上
    if i-1>=0 and j+1<cols:
        if biaozhi[i-1,j+1] == False:
            if image[i-1, j+1] == 255:
                biaozhi[i-1,j+1] = True
            else:
                biaozhi[i-1,j+1] = True
                con.append((i-1,j+1))
                area[0] = min(area[0], i-1)
                area[3] = max(area[3], j+1)
                detect_connect(i-1, j+1, biaozhi, image, rows, cols, con, area)

def adjust(image, cha, WD, HG):
    """ 根据图像，字符区域特征，归一化尺寸，进行分割后的图像归一化调整，得到每个字符的归一化特征适量
    @param image 二值化图片
    @param cha 列表（字符区域像素点和坐标范围）
    @param WD, HG 归一化尺寸
    """
    Ic = []
    N = len(cha)
    # 归一化后角点坐标
    B = np.array([[0, 0, HG-1, HG-1], [0, WD-1, 0, WD-1]])
    for i in range(N):
        pix = cha[i][0]#像素
        p = cha[i][1]#坐标值
        # 图像四个角点坐标
        A = np.array([[p[0], p[0], p[1], p[1]], [p[2], p[3], p[2], p[3]]], dtype = np.float)
        # H*A = B
        H = B@A.T@LA.inv(A@A.T)
        # 对每个字符区域像素点，变换到归一化图像矩阵I
        I = np.full((HG, WD), 255, dtype = np.uint8)
        for pos in pix:
            M = np.array([[pos[0]], [pos[1]]], dtype = np.float)
            m = H@M
            I[np.floor(m[0, 0]), np.floor(m[1, 0])] = 0
        Ic.append(I)
        for j in range(HG):
            for k in range(WD):
                image[j, k+i*WD] = I[j, k]
