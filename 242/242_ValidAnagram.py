class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Solution: 字符串
        # Time: 36ms
        from collections import defaultdict

        dic = defaultdict(int)
        for i in s:
            dic[i] += 1

        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1

        for value in dic.values():
            if value != 0:
                return False

        return True
