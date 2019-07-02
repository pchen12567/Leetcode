def countingSort(nums):
    # 桶的个数
    bucket = [0] * (max(nums) + 1)
    # 将元素值作为键值存储在桶中，记录其出现的次数
    for num in nums:
        bucket[num] += 1
    # nums 的索引
    i = 0
    # 遍历一次所有的"桶"
    for j in range(len(bucket)):
        # 遍历当前"桶"，当"桶"中有数值的时候
        while bucket[j] > 0:
            # 取出当前值
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums


if __name__ == '__main__':
    import time

    print('Start test...')
    start = time.clock()
    nums = [3, 1, 5, 7, 8, 9, 6]
    re = countingSort(nums)
    end = time.clock()
    print(re)
    print('Running time:', end - start)
    print('Test end!')
