class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 双指针
        # Solution 001
        # Time: 44ms
        dic = {}
        for i, n in enumerate(numbers):
            if target - n in dic:
                return [dic[target - n], i + 1]
            else:
                dic[n] = i + 1

        # Solution 002
        # Time: 40ms
        start = 0
        end = len(numbers) - 1
        sum = 0
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]
