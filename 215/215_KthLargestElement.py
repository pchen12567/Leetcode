class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 快速选择、堆排序问题
        # Solution: quick sort
        # Time: 56ms
        import random
        pivot = random.choice(nums)
        left, right = [], []

        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)

        if k <= len(left):
            return self.findKthLargest(left, k)
        if k > len(nums) - len(right):
            return self.findKthLargest(right, k - (len(nums) - len(right)))
        return pivot