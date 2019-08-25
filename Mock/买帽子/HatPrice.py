"""
@Coding: uft-8
@Time: 2019-08-25 23:39
@Author: Ryne Chen
@File: HatPrice.py 
@Python Version: 3.6
"""


def main():
    n = int(input())
    prices = [int(p) for p in input().strip().split()]
    sort_price = sorted(set(prices))
    if len(sort_price) >= 3:
        print(sort_price[2])
    else:
        print(-1)


if __name__ == '__main__':
    main()
