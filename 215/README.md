# 215. Kth Largest Element in an Array
Medium

Find the $k^{th}$ largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1:** <br>
```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2:** <br>
```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```
**Note:**<br> 
You may assume k is always valid, 1 ≤ k ≤ array's length.

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
```