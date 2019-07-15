class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # Time: 152ms
        res = []
        for row in matrix:
            res += row

        return sorted(res)[k - 1]