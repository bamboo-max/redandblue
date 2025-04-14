import random


s = 5
i = 0
p = 9
while i < s :
    n = random.randint(1, 16)  # 生成一个随机数
    if n != p :
        print(n)
        i+= 1



