"""
@Coding: uft-8
@Time: 2019/9/22 2:01 AM
@Author: Ryne Chen
@File: reverseList.py 
@Python Version: 3.6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead

        pre = None
        cur = pHead

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre
