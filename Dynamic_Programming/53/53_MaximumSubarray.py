class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Time: 48ms
        if max(nums) < 0:
            return max(nums)
        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)
        return global_max
