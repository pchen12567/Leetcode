def bubbleSort(nums):
    # 遍历 len(nums)-1 次
    for i in range(len(nums) - 1):
        # 已排好序的部分不用再次遍历
        for j in range(len(nums) - i - 1):
            # 交换位置
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    import time

    print('Start test...')
    start = time.clock()
    nums = [3, 1, 5, 7, 8, 9, 6]
    re = bubbleSort(nums)
    end = time.clock()
    print(re)
    print('Running time:', end - start)
    print('Test end!')
