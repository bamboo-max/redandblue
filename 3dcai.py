import random

#6组前期数据
#previous_list = [654,539,603,67,754,95]
previous_list = [654, 539, 603]

random.seed(2024314)

while_flag = True

counter = 0

while while_flag :
    i = 0
    #t_list = [0,0,0,0,0,0]
    t_list = [0, 0, 0]
    counter  += 1
    while i < 3 :
        t_list[i] = random.randint(0,999)
        i += 1

    print(f"counter={counter}")
    print(t_list)

    if t_list == previous_list or counter > 10000000:
        print(random.randint(0,999))
        while_flag = False

