"""
@Coding: uft-8
@Time: 2019-09-21 01:02
@Author: Ryne Chen
@File: jumpFloorII.py 
@Python Version: 3.6
"""


# 循环思想
def jumpFloorII_iter(number):
    f1 = 1
    if number == 1:
        return f1
    else:
        while number > 1:
            f1 *= 2
            number -= 1
        return f1


# 动态规划思想
def jumpFloorII_dp(number):
    if number == 1:
        return 1
    else:
        record = [1] * number

        for i in range(1, number):
            record[i] = record[i - 1] * 2

        return record[number - 1]


# 递归思想
def jumpFloorII_re(number):
    if number == 1:
        return 1
    else:
        return jumpFloorII_re(number - 1) * 2


def main():
    n = 6

    print(jumpFloorII_iter(n))

    print(jumpFloorII_dp(n))

    print(jumpFloorII_re(n))


if __name__ == '__main__':
    main()
