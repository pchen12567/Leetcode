"""
@Coding: uft-8
@Time: 2019-08-25 18:12
@Author: Ryne Chen
@File: CoinCombination.py 
@Python Version: 003.6
"""

import numpy as np


def combination(coins, n):
    m = len(coins)
    dp = np.zeros((m + 1, n + 1))

    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(j // coins[i - 1] + 1):
                dp[i][j] += dp[i - 1][j - k * coins[i - 1]]

    return int(dp[m][n])


def main():
    coins = [1, 2, 5, 10]
    n = 5

    comb = combination(coins, n)
    print(comb)


if __name__ == '__main__':
    main()
