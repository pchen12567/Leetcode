def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def mergeSort(ls):
    if len(ls) <= 1:
        return ls

    mid_index = len(ls) // 2
    # 递归拆解的过程
    left = mergeSort(ls[:mid_index])
    right = mergeSort(ls[mid_index:])
    # 合并的过程
    return merge(left, right)


if __name__ == '__main__':
    import time

    print('Start test...')
    start = time.clock()
    ls = [3, 1, 5, 7, 8, 9, 6]
    re = mergeSort(ls)
    end = time.clock()
    print(re)
    print('Running time:', end - start)
    print('Test end!')
