import random

red_list_arr = [


    #[4,8,10,21,23,32],
    #[5,14,17,19,20,33],
    #[3,5,9,13,26,29],
    #[1,2,5,9,25,32],
    #[8,10,14,23,28,32],
    #[2,8,11,23,27,29],
    #[10,13,14,23,24,27],
    #[2,5,17,22,30,33],
    #[1,3,4,12,18,24],
    #[2,4,5,10,12,13],
    #[2,13,15,23,27,31],
    #[2,9,12,13,15,24],
    #[1,8,15,20,26,33],
    #[11,12,15,18,25,32],
    #[5,7,12,24,26,28],
    [1,3,5,8,22,33],
    [3,4,9,10,15,22],
    [1,2,4,6,22,30],
    [6,13,17,19,24,31],
    [8,9,14,22,28,30],
    [2,6,11,12,13,33]



]

print(red_list_arr)

m = len(red_list_arr)

red_count_arr = [0]* m ##记录多组数，随机出现的位置（第几次随机出现的）

sum = 0
whil_flag = True ##主循环控制，六组数字全匹配后退出循环

random.seed(7910131618)

while whil_flag :
    red_arr = [0] * 6 ##存储生产的随机数组
    i = 0 ## 控制随机数组下标
    t = 33 ## 控制随机数最大值
    src_arr = list(range(1, 34))  # 初始化一个1~33的列表[1,2,3,......,33]
    while i < 6:
        s = random.randint(0,t-1) #生成一个随机数
        red_arr[i] = src_arr[s]
        src_arr.remove(red_arr[i]) # 移除列表中已经出现过的数值
        i += 1
        t -= 1
    sum += 1
    red_arr.sort()

    for index,val in enumerate(red_list_arr):
        if val == red_arr :
            red_count_arr[index] = sum
            val[0] = 0
            print(f"val={red_count_arr},sum={sum}")

    for val in red_count_arr :
        if val == 0 :
            whil_flag = True
            break
        else :
            whil_flag = False



## 计算前后差值
count = 0 #总合
ave = 0 #平均数

cha_list = [0] * m
p = 0
i = 0
for val in red_count_arr :
    count += val
    cha_list[i] = abs( p - val ) #差值
    p = val
    i += 1
    last_number = val # 获得最后一个数

cha_count = 0 #差值总合
cha_ave = 0  #差值平均数
for val in cha_list :
    cha_count += val
cha_ave = cha_count/m

## 计算最后一个与前面数的差值
#last_count = 0
#last_ave = 0








ave = count/m
print(red_count_arr)
print(f"m={m}")
print(f"cont={count}")
print(f"ave={ave}")
print(cha_list)
print(f"cha_ave={cha_ave}")



random.seed()
print(random.randint(500000,sum))



