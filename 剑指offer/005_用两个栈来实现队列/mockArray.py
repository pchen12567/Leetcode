"""
@Coding: uft-8
@Time: 2019-09-20 01:15
@Author: Ryne Chen
@File: mockArray.py 
@Python Version: 3.6
"""


class Solution:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        self.stack_1.append(node)

    def pop(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()
        return self.stack_2.pop()
