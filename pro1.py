import random

red_list_arr = [

    #[1,14,21,22,23,31],
    #16,21,22,23,27,31],
    #[3,6,19,27,29,33],
    #[9,12,15,18,22,33],
    #[1,2,3,4,17,22],
    #[6,7,10,17,20,26]


    [9,14,18,28,31,33],
    [3,9,11,13,20,32],
    [8,10,13,15,24,31],
    [1,20,21,25,26,27],
    [2,3,8,19,24,30],
    [2,4,8,24,28,31]


]

print(red_list_arr)

m = len(red_list_arr)

red_count_arr = [0]* m ##记录多组数，随机出现的位置（第几次随机出现的）

sum = 0
whil_flag = True ##主循环控制，六组数字全匹配后退出循环

random.seed(2025117)

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




count = 0 #总合
ave = 0 #平均数


for val in red_count_arr :
    count += val

ave = count/m
print(red_count_arr)
print(f"m={m}")
print(f"cont={count}")
print(f"ave={ave}")



random.seed()
print(random.randint(500000,sum))



