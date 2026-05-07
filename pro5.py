import tofivegroup as fg
#根据maxSum的次数，每次生成5组号码完全不重复的双色球号码。
maxSum = 128426

s = 0

while s < maxSum:
    balls = fg.generate_5_red_groups()
    s += 1
    print(balls)

print(f"s={s}")
print(balls)