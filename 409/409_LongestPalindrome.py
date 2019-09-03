class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 字符串问题
        # Solution: O(n), O(001)
        # Time: 20ms
        from collections import defaultdict

        dic = defaultdict(int)

        for c in s:
            dic[c] += 1

        ans = 0

        for value in dic.values():
            ans += value // 2 * 2

            if ans % 2 == 0 and value % 2 == 1:
                ans += 1

        return ans
