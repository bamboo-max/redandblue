import random

#随机产生S个蓝球号，可以屏蔽变量P的号码
p = 13 #要屏蔽的号码
s = 5 #产生多少个蓝球号码
i = 0

while i < s :
    n = random.randint(1, 16)  # 生成一个随机数
    if n != p :
        print(n)
        i+= 1



