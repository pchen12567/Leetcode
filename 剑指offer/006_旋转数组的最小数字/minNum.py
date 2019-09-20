"""
@Coding: uft-8
@Time: 2019-09-20 15:57
@Author: Ryne Chen
@File: minNum.py 
@Python Version: 3.6
"""


# 二分法思想
def minNumberInRotateArray(rotateArray):
    # write code here
    if len(rotateArray) == 0:
        return 0

    left = 0
    right = len(rotateArray) - 1

    while left < right:
        mid = (left + right) // 2
        if rotateArray[mid] > rotateArray[right]:
            left = mid + 1
        elif rotateArray[mid] < rotateArray[right]:
            right = mid
        else:
            right -= 1
    return rotateArray[left]


def main():
    array_1 = [2, 2, 2, 1, 2, 3, 2, 2]
    array_2 = [3, 4, 5, 1, 2]
    array_3 = []

    print(minNumberInRotateArray(array_1))
    print(minNumberInRotateArray(array_2))
    print(minNumberInRotateArray(array_3))


if __name__ == '__main__':
    main()
