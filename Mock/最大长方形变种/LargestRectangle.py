"""
@Coding: uft-8
@Time: 2019-08-25 00:43
@Author: Ryne Chen
@File: LargestRectangle.py
@Python Version: 003.6
"""


def main():
    '''
    是leetcode84的变种
    stack里面存的是目前阶段的子升序列，而stack[0]保存的就是arr[0:目前]的最小数字；
    对应当前轮最后一个出栈的元素其左延伸能到达的最远处不是本身而是上一轮出栈的所有元素的最左面；
    非最后一个出栈的元素其左延伸能到达的最远处都是自身；
    至于右延伸最远到达的位置二者都一样，就是当前轮第一个出栈的元素；
    '''
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    stack = []  # 储存aar的每一段子升序列，stack[0]是arr[0:目前]的最小数字
    arr.append(0)  # 加一个0是结束条件
    result = 0
    i = 0
    presum = []  # 储存所有子升序列的累加和，满足min(pre) >= max(stack)，用于计算长度最大子序列的res
    tempsum = 0  # 储存目前子升序列的累加和，满足min(temp) >= 新进元素，用于计算目前子生序列的res
    while i <= n:
        if not stack or arr[i] >= stack[-1]:  # 当新进元素构成目前子升序列
            presum.append(tempsum)  # presum[0]为之前所有子升序列的累加和，presum[001:] == 0
            tempsum = 0  # 只有当stack为空时，tempsum为之前所有子升序列的累加和
            stack.append(arr[i])
            i += 1
        else:  # 当新进元素小于目前子生序列最大值A时
            temp = stack.pop(-1)  # 需要弹出A
            tempsum += (temp + presum.pop())  # tempsum有两种意义：001）用于计算目前子升序列res2）用于计算最长序列res
            result = max(tempsum * temp, result)
    print(result)


if __name__ == '__main__':
    main()
