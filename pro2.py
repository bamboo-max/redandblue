import random

import random



maxSum = 2083658
#maxSum = random.randint(1000000,10000000)
s = 0
random.seed(20250109)
red_arr = [0] * 6 ##存储生产的随机数组
while s < maxSum:
    red_arr = [0] * 6 ##存储生产的随机数组
    i = 0 ## 控制随机数组下标
    t = 33 ## 控制随机数最大值
    src_arr = list(range(1, 34))  # 初始化一个1~33的列表[1,2,3,......,33]
    while i < 6:
        n = random.randint(0,t-1) #生成一个随机数
        red_arr[i] = src_arr[n]
        src_arr.remove(red_arr[i]) # 移除列表中已经出现过的数值
        i += 1
        t -= 1
    s += 1
    print(s)
    red_arr.sort()
    print(red_arr)

print(maxSum)
print(red_arr)



