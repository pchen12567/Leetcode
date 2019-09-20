"""
@Coding: uft-8
@Time: 2019-09-19 23:22
@Author: Ryne Chen
@File: search.py 
@Python Version: 3.6
"""


def search(array, target):
    i = 0
    j = len(array[0]) - 1

    while i < len(array) and j >= 0:
        start = array[i][j]

        if target == start:
            return True

        elif target > start:
            i += 1

        elif target < start:
            j -= 1

    return False


def main():
    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 4

    print(search(array, target))


if __name__ == '__main__':
    main()
