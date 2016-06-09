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
    # 第四步：去离散杂点噪声,并得到分割后的字符区域特征（像素和范围）
    cha = remove_scatter_noise(img)
    # 第五步：归一化调整
    Ic = adjust(img, cha, WD, HG)
    return (img, cha, Ic)
    
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
    """使用二值滤波，将灰度图转化为二值图像
    @param image 输入的灰度图像
    
    @return img 二值图像
    """
    img = cv2.GaussianBlur(image,(5,5), 0)
    retVal, img = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
    #retVal, img = cv2.threshold(image,200,255,cv2.THRESH_OTSU)
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
    
    @return chal 字符区域描述子列表，（连通像素，区域坐标边界）
    """
    # 图片尺寸
    rows, cols = image.shape
    # 设置判断噪声的长度阈值为30
    LEN = 90
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
            biaozhi[i,j+1] = True
            if image[i,j+1] == 0:
                con.append((i, j+1))
                area[3] = max(area[3],j+1)
                detect_connect(i, j+1, biaozhi, image, rows, cols, con, area)
    #右下
    if i+1<rows and j+1<cols:
        if biaozhi[i+1,j+1] == False:
            biaozhi[i+1,j+1] = True
            if image[i+1,j+1] == 0:
                con.append((i+1,j+1))
                area[1] = max(area[1], i+1)
                area[3] = max(area[3], j+1)
                detect_connect(i+1, j+1, biaozhi, image, rows, cols, con, area)
    #下
    if i+1 < rows:
        if biaozhi[i+1,j] == False:
            biaozhi[i+1,j] = True
            if image[i+1,j] == 0:
                con.append((i+1,j))
                area[1] = max(area[1], i+1)
                detect_connect(i+1, j, biaozhi, image, rows, cols, con, area)
    #左下
    if i+1 <rows and j-1>=0:
        if biaozhi[i+1,j-1] == False:
            biaozhi[i+1,j-1] = True
            if image[i+1,j-1] == 0:
                con.append((i+1,j-1))
                area[1] = max(area[1], i+1)
                area[2] = min(area[2], j-1)
                detect_connect(i+1, j-1, biaozhi, image, rows, cols, con, area)
    #左
    if j-1>=0:
        if biaozhi[i,j-1] == False:
            biaozhi[i,j-1] = True
            if image[i, j-1] == 0:
                con.append((i,j-1))
                area[2] = min(area[2], j-1)
                detect_connect(i, j-1, biaozhi, image, rows, cols, con, area)
    # 左上
    if i-1 >=0 and j-1>=0:
        if biaozhi[i-1,j-1] == False:
            biaozhi[i-1,j-1] = True
            if image[i-1, j-1] == 0:
                con.append((i-1,j-1))
                area[0] = min(area[0], i-1)
                area[2] = min(area[2], j-1)
                detect_connect(i-1, j-1, biaozhi, image, rows, cols, con, area)
    # 上
    if i-1>=0:
        if biaozhi[i-1,j] == False:
            biaozhi[i-1,j] = True
            if image[i-1, j] == 0:
                con.append((i-1,j))
                area[0] = min(area[0], i-1)
                detect_connect(i-1, j, biaozhi, image, rows, cols, con, area)
    # 右上
    if i-1>=0 and j+1<cols:
        if biaozhi[i-1,j+1] == False:
            biaozhi[i-1,j+1] = True
            if image[i-1, j+1] == 0:
                con.append((i-1,j+1))
                area[0] = min(area[0], i-1)
                area[3] = max(area[3], j+1)
                detect_connect(i-1, j+1, biaozhi, image, rows, cols, con, area)

def adjust(image, cha, WD, HG):
    """ 根据图像，字符区域特征，归一化尺寸，进行分割后的图像归一化调整，得到每个字符的归一化特征适量
    @param image 二值化图片
    @param cha 列表（字符区域像素点和坐标范围）
    @param WD, HG 归一化尺寸

    @return Ic 归一化字符特征矩阵列表
    """
    Ic = []
    for i in range(len(cha)):
        pix = cha[i][0]#像素
        p = cha[i][1]#坐标值
        h = HG/(p[1] - p[0])#字符高度缩放因子
        w = WD/(p[3] - p[2])#字符宽度缩放因子
        #存放归一化字符
        I = np.zeros((1, HG*WD),dtype = np.double)
        for pos in pix:
            x = min(int(h*(pos[0] - p[0])), HG-1)
            y = min(int((h+w)/2*(pos[1] - p[2])), WD-1)
            I[0, x*WD+y] = 1
            image[x, y+i*WD] = 0
        Ic.append(I)
    return Ic

def creat_net(H, W):
    """利用随机数，初始化网络参数
    @param H，W输入层的数目，则输入层数为H*W
    
    @return 
    """
    pass
