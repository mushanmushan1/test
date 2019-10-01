import os
import time
from PIL import Image          # 给去除了背景的图像添加背景颜色
from removebg import RemoveBg  # 抠图神器：Remove.bg

print('Start Time: %s' % time.ctime())
time.sleep(1)
print('End   Time: %s' % time.ctime())

# 参数填入 API-Key, 错误日志路径
rmbg = RemoveBg("f7VixBRqAcWpkKY5VmPVu1WL", "./pic/error.log")

# 处理后的图片存放位置
rmbg.remove_background_from_img_file("./pic/Test.png")
# path = os.path.join(os.getcwd(), "pic")
# for pic in os.listdir(path):
#     rmbg.remove_background_from_img_file(os.path.join(path, pic))

# 输入已经去除背景的图像
im = Image.open("./pic/Test.png_no_bg.png")
x, y = im.size

try:
    # 填充红色背景
    p = Image.new("RGBA", im.size, (255, 0, 0))
    p.paste(im, (0, 0, x, y), im)

    # 保存填充后的图片
    p.save("./pic/Test.jpg_red_bg.png")
except:
    with open("./pic/error.log", "a") as f:
        f.write("Background change fail!")

os._exit(0)



while True:
    temp = input('请输入AI问候: ')
    print(temp.replace('吗', '').replace('？', '!'))
