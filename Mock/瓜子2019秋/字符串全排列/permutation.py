"""
@Coding: uft-8
@Time: 2019-08-19 20:03
@Author: Ryne Chen
@File: permutation.py 
@Python Version: 3.6
"""


def permutation(arr, start, end):
    if start == end:
        s = ''.join(arr)
        print(s)
        if s not in string_list:
            print('Not found {}'.format(s))

    else:
        for index in range(start, end):
            arr[index], arr[start] = arr[start], arr[index]
            permutation(arr, start + 1, end)
            arr[index], arr[start] = arr[start], arr[index]


def main():
    global string_list
    # string_list = ['A']
    string_list = ['ABC', 'ACB', 'BAC', 'CAB', 'CBA']
    arr = [i for i in string_list[0]]
    start = 0
    end = len(arr)
    permutation(arr, start, end)


if __name__ == '__main__':
    main()
