def insertionSort(nums):
    # 遍历 len(nums)-1 次
    for i in range(len(nums) - 1):
        # curNum 保存当前待插入的数
        curNum = nums[i + 1]
        # preIndex 保存前一个数的索引
        preIndex = i
        # 将比 curNum 大的元素向后移动
        while curNum < nums[preIndex] and preIndex >= 0:
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        # 待插入的数的正确位置
        nums[preIndex + 1] = curNum
    return nums


if __name__ == '__main__':
    import time

    print('Start test...')
    start = time.clock()
    ls = [3, 1, 5, 7, 8, 9, 6]
    re = insertionSort(ls)
    end = time.clock()
    print(re)
    print('Running time:', end - start)
    print('Test end!')
