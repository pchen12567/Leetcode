"""
@Coding: uft-8
@Time: 2019-08-24 22:05
@Author: Ryne Chen
@File: MaxPointsSet.py 
@Python Version: 3.6
"""

'''
内存超限
case通过率为80.00%
'''

def main():
    n = int(input())
    points = []

    for p in range(n):
        x, y = [int(x) for x in input().strip().split()]
        points.append((x, y))

    print(points)

    sort_points = sorted(points, key=lambda x: (x[0], x[1]), reverse=True)
    # sort_points = sorted(points, reverse=True)

    print(sort_points)

    tmp = -1
    res = []
    for point in sort_points:
        if point[1] > tmp:
            res.append((point[0], point[1]))
            tmp = point[1]

    res = sorted(res)
    for p in res:
        print(p[0], p[1])


if __name__ == '__main__':
    main()
