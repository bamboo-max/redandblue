import random

red_list_arr = [
    #[15,16,20,22,23,29],
    #[4,7,8,17,22,26],
    #[1,2,7,15,24,29],
    #[4,6,13,21,22,25],
    #[2,5,11,22,30,33],
    #[2,9,11,17,20,30],
    #[1,3,16,22,23,30],
    #[2,4,11,22,27,32],
    #[5,11,13,16,21,30],
    #[2,6,15,16,21,23],
    [3,9,16,17,18,22],
    [13,14,20,22,26,32],
    [5,10,16,19,29,32],
    [2,3,17,18,22,33],
    [9,12,13,15,22,26],
    [10,19,20,26,28,29],
    [3,7,17,27,29,32],
    [10,16,19,27,28,30]


]

print(red_list_arr)

m = len(red_list_arr)

red_count_arr = [0]* m ##记录八组数，随机出现的位置（第几次随机出现的）

sum = 0
whil_flag = True ##主循环控制，六组数字全匹配后退出循环

random.seed(2025006)

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




print(random.randint(64295,4330385))



