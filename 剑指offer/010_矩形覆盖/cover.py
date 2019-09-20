"""
@Coding: uft-8
@Time: 2019-09-21 02:06
@Author: Ryne Chen
@File: cover.py 
@Python Version: 3.6
"""


# 循环思想
def rectCover_iter(number):
    f1 = 1
    f2 = 2
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        while number > 2:
            f1, f2 = f2, f1 + f2
            number -= 1
        return f2


# 动态规划思想
def rectCover_dp(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        record = [1] * number
        record[1] = 2

        for i in range(2, number):
            record[i] = record[i - 1] + record[i - 2]

        return record[number - 1]


# 递归思想
def rectCover_re(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return rectCover_re(number - 1) + rectCover_re(number - 2)


def main():
    n = 5

    print(rectCover_iter(n))

    print(rectCover_dp(n))

    print(rectCover_re(n))


if __name__ == '__main__':
    main()
