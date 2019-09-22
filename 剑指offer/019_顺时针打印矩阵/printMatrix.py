"""
@Coding: uft-8
@Time: 2019/9/22 6:34 PM
@Author: Ryne Chen
@File: printMatrix 
@Python Version: 3.6
"""


def printMatrix(matrix):
    res = []

    # 按顺时针每圈循环输出每个数字
    while matrix:
        # 从左向右依次输出第一排的每个数字
        res += matrix.pop(0)

        # 从上至下依次输出剩下每排的最后一个数字
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())

        # 从右向左依次输出最后一排剩下的每个数字
        if matrix:
            res += matrix.pop()[::-1]

        # 从下至上依次输出剩下每排的第一个数字，至此完全一圈的输出
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))

    return res


def main():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(printMatrix(matrix))


if __name__ == '__main__':
    main()
