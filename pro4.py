import tofivegroup as fg

import pandas as pd


loopnum = 5
df = pd.read_excel("xsq.xlsx")
data1 = df.tail(loopnum) #读取文件后15行
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




s = 0
sumdata = 0
while s < loopnum:
    i = 0
    value = True
    balls = fg.generate_5_red_groups()
    while value :
        balls = fg.generate_5_red_groups()
        i = i+1
        f = fg.group_exists(red_list_arr[s], balls)
        if f :
            value = False
            s += 1
            sumdata += i
            print(i)


print(f"平均数为：{sumdata/loopnum}")