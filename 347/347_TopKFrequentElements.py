class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # # Solution 1:
        # # Time: 104ms
        # # Complexity: <= O(nlogn)
        # from collections import defaultdict
        # dic = defaultdict(int)
        # for num in nums:
        #     dic[num] += 1
        # sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        # return [key for (key,value) in sort_dic[:k]]

        # 桶排序问题
        # Solution 2: Bucket Sort
        # Time: 92ms
        # Complexity: O(n)
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in dic.items():
            bucket[value].append(key)
        res = []
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]
