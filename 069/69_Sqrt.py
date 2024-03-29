class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # 二分
        # Solution：O(nlogN）
        # Time: 12ms
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
