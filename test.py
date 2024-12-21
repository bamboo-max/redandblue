import random


'''a = 0
while (a != 5):
    a = random.randint(1,33)
    print(a)


arr = [1] * 10  #初始化一个包含10个0的列表（数组）
arr[2] =50
arr[4] =50
print(arr)
print(len(arr))
arr.remove(50)  #删除列表中第一个值为50的元素
print(arr)
print(len(arr))
arr.remove(50)  #删除列表中第一个值为50的元素
print(arr)
print(len(arr))'''


red_arr0 = [1,4,25,27,28,33]
red_arr1 = [1,8,12,17,19,24]
red_arr2 = [9,10,13,19,24,32]
red_arr3 = [1,8,13,18,20,26]
red_arr4 = [2,5,13,20,27,32]
red_arr5 = [14,18,23,24,26,33]

red_list_arr = [red_arr0,red_arr1,red_arr2,red_arr3,red_arr4,red_arr5]

print(red_list_arr)

for index,val in enumerate(red_list_arr):
    print(index,val)
