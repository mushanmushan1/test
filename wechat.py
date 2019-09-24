import cv2


# 读取头像和国旗图案
img_head = cv2.imread("wf_head.jpg")
img_flag = cv2.imread("flag.jpg")

# 获取头像和国旗图案宽、高
w_head, h_head = img_head.shape[:2]  # [0:3]图片的宽 高 颜色通道
w_flag, h_flag = img_flag.shape[:2]

# 计算图案缩放比例
scale = w_head / w_flag / 4

# 缩放图案
img_flag = cv2.resize(img_flag, (0, 0), fx=scale, fy=scale)

# 获取缩放后新宽度
w_flag, h_flag = img_flag.shape[:2]  # 注意width在前 height在后

# 按3个通道合并图片
for c in range(0, 3):
    img_head[w_head-w_flag:, h_head-h_flag:, c] = img_flag[:, :, c]

# 保存最终结果
cv2.imwrite("new_head.jpg", img_head)

# 显示=最终图片
img = cv2.imread("new_head.jpg")
cv2.namedWindow("Image", 0)
cv2.resizeWindow("Image", 500, 500)  # 创建一个500*500大小的窗口
cv2.imshow("Image", img)
cv2.waitKey(0)                       # 如果不添该命令，在IDE中执行窗口直接无响应。在命令行中执行的话，则是一闪而过
cv2.destroyAllWindows()              # 释放窗口是个好习惯！