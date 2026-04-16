import random

import pandas as pd


df = pd.read_excel("xsq.xlsx")
data1 = df.tail(15) #读取文件后15行
rows_as_dicts = data1.to_dict(orient='records') #将读取DataFrame 对象转换为字典
red_list_arr = []

for val in rows_as_dicts:
    #print(val)
    #print(val["redstr"])
    str_list = val["redstr"].split(",") #将字符串按逗号分拆并存成一个列表
    int_list = [int(x) for x in str_list] #将列表中的字符串转为数字
    red_list_arr.append(int_list)

"""
red_list_arr = [[1,2,4,6,22,30],[6,13,17,19,24,31]]
"""
print(red_list_arr)



m = len(red_list_arr)

red_count_arr = [0]* m ##记录多组数，随机出现的位置（第几次随机出现的）

sum = 0
whil_flag = True ##主循环控制，六组数字全匹配后退出循环

random.seed(78070910131816)

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


cha_count = 0 #差值总合
cha_ave = 0  #差值平均数
for val in cha_list :
    cha_count += val
cha_ave = cha_count/m

## 计算最后一个与前面数的差值
last_count = 0
last_ave = 0
last_list = [0] * m
last_number = red_count_arr[m-1] # 获得最后一个数
i = 0
for val in red_count_arr :
    last_list[i] = abs(val -  last_number)
    i += 1












ave = count/m
print(red_count_arr)
print(f"m={m}")
print(f"cont={count}")
print(f"ave={ave}")
print(cha_list)
print(f"cha_ave={cha_ave}")
print(f"last_list={last_list}")



random.seed()
print(f"s={random.randint(500000,sum)}")



