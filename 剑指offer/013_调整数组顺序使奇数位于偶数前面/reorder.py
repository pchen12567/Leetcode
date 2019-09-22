"""
@Coding: uft-8
@Time: 2019/9/21 9:01 PM
@Author: Ryne Chen
@File: reorder.py 
@Python Version: 3.6
"""


# 思路一：2n个额外空间
def reOrderArray_1(array):
    ls_odd = []
    ls_even = []
    for i in array:
        if i % 2 == 1:
            ls_odd.append(i)
        else:
            ls_even.append(i)
    return ls_odd + ls_even


# 思路二：1n个额外空间
def reOrderArray_2(array):
    result = []
    odd_point = 0
    for i in array:
        if i % 2 == 0:
            result.append(i)
        else:
            result.insert(odd_point, i)
            odd_point += 1
    return result


# 思路三：不使用额外空间
def reOrderArray_3(array):
    point_i = 0
    iter_count = 0

    while iter_count < len(array):
        if array[point_i] % 2 == 0:
            temp = array[point_i]
            point_j = point_i
            while point_j + 1 < len(array):
                array[point_j] = array[point_j + 1]
                point_j += 1
            array[-1] = temp
        else:
            point_i += 1
        iter_count += 1
    return array


# 思路四: 双指针，不改变相对位置
def reOrderArray_4(array):
    pivot = 0
    for i in range(len(array)):
        if array[i] % 2 == 1:
            p_search = i
            while p_search > pivot:
                array[p_search], array[p_search - 1] = array[p_search - 1], array[p_search]
                p_search -= 1

            pivot += 1
    return array


# 思路五：双指针，但是会改变相对位置
def reOrderArray_5(array):
    p_even = 0
    p_odd = len(array) - 1

    while p_even < p_odd:
        while p_even < p_odd:
            if array[p_even] % 2 != 0:
                p_even += 1
            else:
                break
        while p_even < p_odd:
            if array[p_odd] % 2 != 1:
                p_odd -= 1
            else:
                break
        array[p_even], array[p_odd] = array[p_odd], array[p_even]
    return array


def main():
    array = [4, 2, 5, 6, 3, 8, 7]

    print(reOrderArray_1(array))

    print(reOrderArray_2(array))

    print(reOrderArray_3(array))

    print(reOrderArray_4(array))

    print(reOrderArray_5(array))


if __name__ == '__main__':
    main()
