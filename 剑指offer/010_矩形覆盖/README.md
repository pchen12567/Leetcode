## 题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 * 1的小矩形无重叠地覆盖一个2 * n的大矩形，总共有多少种方法？

## 思路
通过归纳法，可以得到：<br>
n= 1时，f(1) = 1 <br>
n= 2时，f(2) = 2 <br>
n= 3时，f(3) = 3 <br>
n= 4时，f(4) = 5 <br>
n= 5时，f(5) = 8 

标准的斐波那契数列，故可用斐波那契数列解决: <br>
f(n) = f(n-1) + f(n-2)， (n > 2)。

可以尝试将题目改成1 * 3方块覆盖3 * n、1 * 4方块覆盖4 * n。<br>
相应的结论应该是：
- 1 * 3方块覆盖 3*n 区域：f(n) = f(n-1) + f(n - 3)， (n > 3)
- 1 * 4方块覆盖 4*n 区域：f(n) = f(n-1) + f(n - 4)，(n > 4)

更一般的结论，如果用1 * m的方块覆盖m * n区域，递推关系式为f(n) = f(n-1) + f(n-m)，(n > m)。