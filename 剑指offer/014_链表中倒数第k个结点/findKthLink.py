"""
@Coding: uft-8
@Time: 2019/9/22 1:31 AM
@Author: Ryne Chen
@File: findKthLink 
@Python Version: 3.6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None

        # 设置两个指针
        p1 = head
        p2 = head

        # p2先走，走k-1步，如果k大于链表长度则返回空，否则的话继续走
        while k > 1:
            if p2.next:
                p2 = p2.next
                k -= 1
            else:
                return None

        # 两个指针一起走，一直到p2为最后一个,p1即为所求
        while p2.next:
            p2 = p2.next
            p1 = p1.next

        return p1
