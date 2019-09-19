import random
secret = random.randint(1, 10)
print("---- I love U! ----")
temp = input("不妨猜一下小甲鱼现在心里想的是哪一个数字：")
guess = int(temp)

# TODO Game Begin!
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("卧槽，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束了，不玩啦^_^")


