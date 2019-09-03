"""
@Coding: uft-8
@Time: 2019-08-25 23:50
@Author: Ryne Chen
@File: ShortestDistance.py 
@Python Version: 3.6
"""


def distance(start, end):
    return abs(end - start)


def main():
    n = int(input())
    points = [int(p) for p in input().strip().split()]

    dist_list = []
    for p in points[1:-1]:
        tmp = points.copy()
        tmp.remove(p)

        dist = 0
        for i in range(len(tmp)-1):
            dist += distance(tmp[i], tmp[i+1])

        dist_list.append(dist)

    print(min(dist_list))


if __name__ == '__main__':
    main()
