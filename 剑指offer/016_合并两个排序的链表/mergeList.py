"""
@Coding: uft-8
@Time: 2019/9/22 5:43 PM
@Author: Ryne Chen
@File: mergeList.py 
@Python Version: 3.6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    # 思路一：递归思想
    def Merge_1(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        elif pHead1.val <= pHead2.val:
            pHead1.next = self.Merge_1(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge_1(pHead1, pHead2.next)
            return pHead2

    # 思路二：新开链表，比较大小存储
    def Merge_2(self, pHead1, pHead2):
        pHead = ListNode(0)
        cur = pHead

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                cur = cur.next
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                cur = cur.next
                pHead2 = pHead2.next

        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2

        return pHead.next
