"""
@Coding: uft-8
@Time: 2019-09-20 17:52
@Author: Ryne Chen
@File: fibonacci.py 
@Python Version: 3.6
"""


# 动态规划思想
def Fibonacci_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        record = [0] * (n + 1)
        record[1] = 1

        for i in range(2, n + 1):
            record[i] = record[i - 1] + record[i - 2]

        return record[n]


# 递归思想
def Fibonacci_re(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_re(n - 1) + Fibonacci_re(n - 2)


# 循环思想
def Fibonacci_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f1, f2 = 0, 1
        while n > 1:
            f2, f1 = f1 + f2, f2
            n -= 1
        return f2


# 生成器
def Fibonacci_gen(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        f2, f1 = f1 + f2, f2
        yield f1


def main():
    n = 10
    print(Fibonacci_dp(n))

    print(Fibonacci_re(n))

    print(Fibonacci_iter(n))

    print([i for i in Fibonacci_gen(n)][-1])


if __name__ == '__main__':
    main()
