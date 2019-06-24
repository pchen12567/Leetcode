class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Solution 1
        # Time: 4580ms
        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i + 1:]):
                if first + second == target:
                    return [i, i + 1 + j]

        # Solution 2
        # Time: 40ms
        hashed = {}
        for i, n in enumerate(nums):
            hashed[n] = i
        for i, n in enumerate(nums):
            if target - n in hashed and hashed[target - n] != i:
                return [i, hashed[target - n]]

        # Solution 3
        # Time: 32ms
        hashed = {}
        for i, n in enumerate(nums):
            if target - n in hashed:
                return [hashed[target - n], i]
            else:
                hashed[n] = i
