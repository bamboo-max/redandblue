import random

red_list_arr = [

    #[9,12,13,24,25,33],
    #[10,11,22,27,30,32],
    #[12,15,21,23,25,30],
    #[9,10,12,14,19,32],
    #[5,7,8,15,16,23],
    #[4,9,14,15,18,25],
    [5,15,16,25,30,33],
    [4,6,7,30,31,33],
    [1,5,6,8,23,28],
    [3,8,10,14,16,21],
    [3,5,18,25,26,33],
    [5,8,13,14,24,26],
    [1,8,16,18,25,31]

]

print(red_list_arr)

m = len(red_list_arr)

red_count_arr = [0]* m ##记录八组数，随机出现的位置（第几次随机出现的）

sum = 0
whil_flag = True ##主循环控制，六组数字全匹配后退出循环

random.seed(2025034)

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




print(random.randint(124969,1954839))



