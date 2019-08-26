"""
@Coding: uft-8
@Time: 2019-08-26 16:39
@Author: Ryne Chen
@File: Permute.py 
@Python Version: 3.6
"""


def permute(n, k):
    cur_d = {i: 1 for i in range(n - k)}
    print(cur_d)

    pre_d = {}
    for j in range(1, k + 1):
        pre_d = cur_d
        cur_d = {0: 1}
        for i in range(1, n - k):
            cur_d[i] = pre_d[i] * (i + 1) + cur_d[i - 1] * (j + 1)
    return cur_d[n - k - 1] % 2017


def main():
    n, k = [int(x) for x in input().strip().split()]
    res = permute(n, k)
    print(res)


if __name__ == '__main__':
    main()
