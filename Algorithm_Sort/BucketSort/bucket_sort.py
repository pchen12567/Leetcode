from InsertionSort import insertion_sort


def bucketSort(nums, defaultBucketSize=5):
    # 获取数组中的最大最小值
    minVal, maxVal = min(nums), max(nums)

    # 如果没有指定桶的大小，则默认为5
    bucketSize = defaultBucketSize

    # 数据分为 bucketCount 组
    bucketCount = (maxVal - minVal) // bucketSize + 1

    # 二维桶
    buckets = []
    for i in range(bucketCount):
        buckets.append([])

    # 利用函数映射将各个数据放入对应的桶中
    for num in nums:
        buckets[(num - minVal) // bucketSize].append(num)

    # 清空 nums
    nums.clear()

    # 对每一个二维桶中的元素进行排序
    for bucket in buckets:
        # 假设使用插入排序
        bucket = insertion_sort.insertionSort(bucket)

        # 将排序好的桶依次放入到 nums 中
        nums.extend(bucket)

    return nums


if __name__ == '__main__':
    import time

    print('Start test...')
    start = time.clock()
    nums = [3, 1, 5, 7, 8, 9, 6]
    re = bucketSort(nums)
    end = time.clock()
    print(re)
    print('Running time:', end - start)
    print('Test end!')
