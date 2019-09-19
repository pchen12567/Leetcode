"""
@Coding: uft-8
@Time: 2019-09-20 00:31
@Author: Ryne Chen
@File: printLinkedList.py 
@Python Version: 3
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 递归思想
class Solution_1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]


# 数组翻转思想
class Solution_2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ls = []
        while listNode is not None:
            ls.append(listNode.val)
            listNode = listNode.next
        return [i for i in ls[::-1]]


# 栈思想
# 1.先遍历链表元素到栈
# 2.栈再弹出
class Solution_3:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ls_in = []
        ls_out = []
        while listNode:
            ls_in.append(listNode.val)
            listNode = listNode.next
        while ls_in:
            ls_out.append(ls_in.pop())
        return ls_out
