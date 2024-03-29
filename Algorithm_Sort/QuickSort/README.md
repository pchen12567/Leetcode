# Quick Sort 快速排序
快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，
则可分别对这两部分记录继续进行排序，以达到整个序列有序。

又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。
它是处理大数据最快的排序算法之一，虽然最差情况的时间复杂度达到了$O(n^2)$，
但是在大多数情况下都比平均时间复杂度为$O(n\log(n))$的排序算法表现要更好，因为$O(n\log(n))$记号中隐含的常数因子很小，
而且快速排序的内循环比大多数排序算法都要短小，这意味着它无论是在理论上还是在实际中都要更快，
比复杂度稳定等于$O(n\log(n))$的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
它的主要缺点是非常脆弱，在实现时要非常小心才能避免低劣的性能。

## 算法描述
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

1. 从数列中挑出一个元素，称为 “基准”（pivot）；
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

## 算法分析
1. 平均时间复杂度：$O(n\log(n))$。
2. 最好情况：$O(n\log(n))$。
3. 最坏情况：$O(n^2)$。
4. 空间复杂度：$O(\log(n))$。
5. 稳定性：不稳定。

## 动图演示
![](https://github.com/pchen12567/picture_store/blob/master/Algorithm/quickSort_01.gif?raw=true)
