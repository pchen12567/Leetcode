class Solution(object):
    # Solution1: Fibonacci
    # Time: 16ms
    def climbStairs_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current

    # Solution2: DP
    # Time: 16ms
    def climbStairs_2(self, n):
        if n == 1:
            return 1
        res = [-1 for _ in range(n)]
        res[0] = 1
        res[1] = 2
        return self.dp(n - 1, res)

    def dp(self, n, res):
        if res[n] == -1:
            res[n] = self.dp(n - 1, res) + self.dp(n - 2, res)
        return res[n]
