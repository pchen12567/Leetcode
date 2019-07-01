def selectionSort(nums):
    # 遍历 len(nums)-1 次
    for i in range(len(nums) - 1):
        # 初始化最小值索引
        min_index = i
        # 遍历剩下的nums
        for j in range(i + 1, len(nums)):
            # 找到最小值的索引
            if nums[j] < nums[min_index]:
                # 更新最小值索引
                min_index = j
        # 把最小数交换到前面
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == '__main__':
    import time

    print('Start test...')
    start = time.clock()
    nums = [3, 1, 5, 7, 8, 9, 6]
    re = selectionSort(nums)
    end = time.clock()
    print(re)
    print('Running time:', end - start)
    print('Test end!')
