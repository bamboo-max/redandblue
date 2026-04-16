import tofivegroup as fg

maxSum = 262791

s = 0

while s < maxSum:
    balls = fg.generate_5_red_groups()
    s += 1
    print(balls)

print(f"s={s}")
print(balls)