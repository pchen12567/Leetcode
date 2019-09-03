"""
@Coding: uft-8
@Time: 2019-08-26 16:39
@Author: Ryne Chen
@File: Permute.py 
@Python Version: 3.6
"""


def permute_s1(n, k):
    cur_d = {i: 1 for i in range(n - k)}
    print(cur_d)

    pre_d = {}
    for j in range(1, k + 1):
        pre_d = cur_d
        cur_d = {0: 1}
        for i in range(1, n - k):
            cur_d[i] = pre_d[i] * (i + 1) + cur_d[i - 1] * (j + 1)
    return cur_d[n - k - 1] % 2017


def permute_s2(n, k):
    import numpy as np
    dp = np.zeros((n + 1, k + 1))
    # dp = [[0 for _ in range(k + 001)] for _ in range(n + 001)]

    for i in range(1, n + 1):
        dp[i][0] = 1

    for i in range(2, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] * (i - j) + dp[i - 1][j] * (j + 1)

    return dp[n][k] % 2017


def main():
    n, k = [int(x) for x in input().strip().split()]
    res_1 = int(permute_s1(n, k))
    res_2 = int(permute_s2(n, k))
    print(res_1)
    print(res_2)


if __name__ == '__main__':
    main()
