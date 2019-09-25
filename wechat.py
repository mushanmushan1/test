import sys
import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()  # 返回值 return, 图像 frame
        cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)           # 响应时间：50ms
        if c == 27:
            break


def get_image_info(image):
    print(type(image))      # <class 'numpy.ndarray'>
    print(image.shape)      # (1209, 1242, 3)
    print(image.size)       # 4504734
    print(image.dtype)      # uint8


# 读取头像和国旗图案
img_head = cv.imread("head.jpg")
img_flag = cv.imread("flag.jpeg")

get_image_info(img_head)    # 获取图像信息
sys.exit(0)

# 获取头像和国旗图案宽、高
w_head, h_head = img_head.shape[:2]  # [0:3]图片的宽 高 颜色通道
w_flag, h_flag = img_flag.shape[:2]

# 计算图案缩放比例
scale = w_head / w_flag / 4

# 缩放图案
img_flag = cv.resize(img_flag, (0, 0), fx=scale, fy=scale)

# 获取缩放后新宽度
w_flag, h_flag = img_flag.shape[:2]  # 注意width在前 height在后

# 按3个通道合并图片
for c in range(0, 3):
    img_head[w_head-w_flag:, h_head-h_flag:, c] = img_flag[:, :, c]

# 保存最终结果
cv.imwrite("new_head.jpg", img_head)

# 显示=最终图片
img = cv.imread("new_head.jpg")
cv.namedWindow("Image", 0)
cv.resizeWindow("Image", 500, 500)  # 创建一个500*500大小的窗口
cv.imshow("Image", img)
cv.waitKey(0)                       # 如果不添该命令，在IDE中执行窗口直接无响应。在命令行中执行的话，则是一闪而过
cv.destroyAllWindows()              # 释放窗口是个好习惯！