"""
@Coding: uft-8
@Time: 2019/9/25 7:56 PM
@Author: Ryne Chen
@File: minStack.py 
@Python Version: 3.6
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)

        if not self.min_stack:
            self.min_stack.append(node)
        else:
            if node < self.min_stack[-1]:
                self.min_stack.append(node)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
