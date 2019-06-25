class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        pointer = 0
        maxLen = 0
        for index, value in enumerate(s):
            if value in dic:
                pointer = max(dic[value] + 1, pointer)
            maxLen = max(index - pointer + 1, maxLen)
            dic[value] = index
        return maxLen
