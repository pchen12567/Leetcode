"""
@Coding: uft-8
@Time: 2019/9/25 8:52 PM
@Author: Ryne Chen
@File: popOrder.py 
@Python Version: 3.6
"""


def IsPopOrder(pushV, popV):
    stack = []
    i = 0

    for v in pushV:
        stack.append(v)

        while stack and stack[-1] == popV[i]:
            stack.pop()
            i += 1

    if not stack:
        return True
    else:
        return False


def main():
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]

    print(IsPopOrder(pushV, popV))


if __name__ == '__main__':
    main()
