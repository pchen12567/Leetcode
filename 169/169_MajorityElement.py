class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 多数投票问题
        # Time: 144ms
        from collections import defaultdict

        dic = defaultdict(int)

        for n in nums:
            dic[n] += 1

        for key, value in dic.items():
            if value > len(nums) / 2:
                return key