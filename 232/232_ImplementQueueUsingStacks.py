class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._s1, self._s2 = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self._s1:
            self._s2.append(self._s1.pop())
        self._s1.append(x)
        while self._s2:
            self._s1.append(self._s2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self._s1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self._s1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self._s1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# 栈和队列问题
