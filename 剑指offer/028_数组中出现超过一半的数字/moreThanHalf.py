"""
@Coding: uft-8
@Time: 2019/9/25 11:30 PM
@Author: Ryne Chen
@File: moreThanHalf.py 
@Python Version: 3.6
"""


def MoreThanHalfNum_Solution(numbers):
    # write code here
    dic = {}

    for n in numbers:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1

    for key in dic:
        if dic[key] > len(numbers) / 2:
            return key

    return 0


def main():
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(MoreThanHalfNum_Solution(numbers))


if __name__ == '__main__':
    main()
