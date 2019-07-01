def quickSort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]

    left = [nums[i] for i in range(1, len(nums)) if nums[i] < pivot]
    right = [nums[i] for i in range(1, len(nums)) if nums[i] >= pivot]

    return quickSort(left) + [pivot] + quickSort(right)


if __name__ == '__main__':
    import time

    print('Start test...')
    start = time.clock()
    nums = [3, 1, 5, 7, 8, 9, 6]
    re = quickSort(nums)
    end = time.clock()
    print(re)
    print('Running time:', end - start)
    print('Test end!')
