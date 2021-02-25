'''无价之姐  致敬唐哥'''
import os
import time
import cv2
import base64
import numpy as np
from aip import AipBodyAnalysis
import random

'''一、自动化下载需要的库'''
# bags = {"lxml","requests","pandas","numpy","you-get","opencv-python","pandas","fake_useragent","matplotlib","moviepy","lxml","wordcloud","jieba"}
# try:
#     for bag in bags:
#         os.system(f"pip3 install -i https://pypi.doubanio.com/simple/{bag}")
#         print(bag+"库下载成功")
# except:
#     print(bag+"库下载失败")

'''视频下载'''
'''使用you-get方法在cmd命令台中下载'''

'''视频分割'''
# cap = cv2.VideoCapture(r"D:\blibli\超A美少女带你乘风破浪❤️【欣小萌】 (P1. 横屏版).flv".replace('\\', '/'))
# num = 1
# while 1:
#     # 逐帧读取视频  按顺序保存到本地文件夹
#     ret,frame = cap.read()
#     if ret:
#         cv2.imwrite(f"D:/blibli/priceless/img_{num}.jpg",frame)
#         print(cv2.imwrite(f"D:/blibli/priceless/img_{num}.jpg",frame))
#         num+=1
#     else:
#         print("结束")
#         break
# cap.release()   # 释放资源


'''人像分割'''
APP_ID = '23679655'
API_KEY = '1Ea5FhZ66Va27wifoh4EQG5p'
SECRET_KEY = 'j4mDL1vOxaVHLbvUSLkS5ITxXTeETf5Y'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
# 保存图像分割后的路径
path = 'D:/blibli/whole/'

# os.listdir  列出保存到图片名称
img_files = os.listdir('D:/blibli/priceless/')
print(img_files)

for num in range(1, 3668):
    # 按顺序构造出图片路径
    img = f'D:/blibli/priceless/img_{num}.jpg'
    img1 = cv2.imread(img)
    height, width, _ = img1.shape
    print(height, width)
    print(img)
    # 二进制方式读取图片
    with open(img, 'rb') as fp:
        img_info = fp.read()

    # 设置只返回前景   也就是分割出来的人像
    seg_res = client.bodySeg(img_info)
    labelmap = base64.b64decode(seg_res['labelmap'])
    nparr = np.frombuffer(labelmap, np.uint8)
    labelimg = cv2.imdecode(nparr, 1)
    labelimg = cv2.resize(labelimg, (width, height), interpolation=cv2.INTER_NEAREST)
    new_img = np.where(labelimg == 1, 255, labelimg)
    mask_name = path + 'mask_{}.png'.format(num)
    # 保存分割出来的人像
    cv2.imwrite(mask_name, new_img)
    print(f'======== 第{num}张图像分割完成 ========')

