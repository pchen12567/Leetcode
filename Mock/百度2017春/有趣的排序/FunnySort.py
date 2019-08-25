"""
@Coding: uft-8
@Time: 2019-08-26 00:08
@Author: Ryne Chen
@File: FunnySort.py 
@Python Version: 3.6
"""


def main():
    n = int(input())
    nums = [int(n) for n in input().strip().split()]

    index = sorted(range(len(nums)), key=lambda i: nums[i])

    count = 1
    for i in range(1, len(index)):
        if index[i] > index[i - 1]:
            count += 1
        else:
            break

    print(len(index) - count)


if __name__ == '__main__':
    main()
