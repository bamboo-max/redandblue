import random



#red_arr0 = [4,5,11,15,20,32]

#red_arr0 = [1,4,25,27,28,33]
#red_arr1 = [1,11,15,27,30,33]
#red_arr0 = [2,4,13,16,18,20]
#red_arr1 = [5,11,17,18,30,31]
#red_arr2 = [3,11,15,20,25,26]
#red_arr0 = [4,9,10,19,26,27]
#red_arr0 = [2,7,11,21,27,28]
#red_arr0 = [15,16,20,22,23,29]
red_arr0 = [4,7,8,17,22,26]
red_arr1 = [1,2,7,15,24,29]
red_arr2 = [4,6,13,21,22,25]
red_arr3 = [2,5,11,22,30,33]
red_arr4 = [2,9,11,17,20,30]
red_arr5 = [1,3,16,22,23,30]



red_list_arr = [red_arr0,red_arr1,red_arr2,red_arr3,red_arr4,red_arr5]

print(red_list_arr)

red_count_arr = [0]* 6 ##记录六组数，随机出现的位置（第几次随机出现的）

sum = 0
whil_flag = True ##主循环控制，六组数字全匹配后退出循环

random.seed(2024146)

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

ave = count/6
print(red_count_arr)
print(f"cont={count}")
print(f"ave={ave}")




print(random.randint(17741,4340336))



