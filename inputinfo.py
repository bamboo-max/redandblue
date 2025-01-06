
#red1 = input("输入红球1：")
#print("红球1：",int(red1))

#a,b = input("请输入两个红球号，用‘,’号隔开：").split(",")
#print(f"a={a},b={b}")

print("请输入红球：")
i = 0
reds = []
while (i < 6) :
    t_red = 0
    reds.append(int(input(f"请输入红球{i+1}:")))

    i += 1
reds.sort()
print(reds)