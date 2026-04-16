import random


def generate_unique_double_color_balls(group_num=5):
    # 双色球红球范围 1-33，蓝球 1-16
    all_red = set()
    result = []

    while len(result) < group_num:
        # 随机生成6个不重复红球
        red_balls = random.sample(range(1, 34), 6)
        red_balls.sort()
        # 转集合判断全局是否重复
        red_set = set(red_balls)
        # 组内号码 和 已出现过的所有红球 无交集才合法
        if red_set.isdisjoint(all_red):
            all_red.update(red_set)
            # 随机蓝球
            blue_ball = random.randint(1, 16)
            result.append({"红球": red_balls, "蓝球": blue_ball})
    return result


def generate_5_red_groups():
    # 所有可选红球
    all_reds = list(range(1, 34))
    # 随机打乱
    random.shuffle(all_reds)

    groups = []
    # 每6个一组，取5组
    for i in range(5):
        start = i * 6
        end = start + 6
        group = sorted(all_reds[start:end])  # 每组内部升序
        groups.append(group)

    return groups

def group_exists(target, groups):
    target_set = set(target)
    for g in groups:
        if target_set.issubset(set(g)):
            return True
    return False


if __name__ == "__main__":

    balls2 = generate_5_red_groups()
    print(balls2)

    balls = generate_unique_double_color_balls(5)

    print(balls)
    print("=== 5组双色球（全部红球无重复）===")
    for idx, item in enumerate(balls, 1):
        print(f"第{idx:02d}组 红球：{item['红球']}  蓝球：{item['蓝球']}")