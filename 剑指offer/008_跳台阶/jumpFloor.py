"""
@Coding: uft-8
@Time: 2019-09-20 18:49
@Author: Ryne Chen
@File: jumpFloor.py 
@Python Version: 3.6
"""


# 循环思想
def jumpFloor_iter(number):
    f1 = 1
    f2 = 2

    if number == 1:
        return f1
    elif number == 2:
        return f2
    else:
        while number > 2:
            f1, f2 = f2, f1 + f2
            number -= 1
        return f2


# 递归思想
def jumpFloor_re(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return jumpFloor_re(number - 1) + jumpFloor_re(number - 2)


# 动态规划思想
def jumpFloor_dp(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        record = [1] * number
        record[1] = 2

        for i in range(2, number):
            record[i] = record[i - 1] + record[i - 2]
        return record[number - 1]


def main():
    n = 4

    print(jumpFloor_iter(n))

    print(jumpFloor_re(n))

    print(jumpFloor_dp(n))


if __name__ == '__main__':
    main()
