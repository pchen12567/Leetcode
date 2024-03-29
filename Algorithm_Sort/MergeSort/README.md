# Merge Sort 归并排序

归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
若将两个有序表合并成一个有序表，称为2路归并。

## 算法描述
1. 把长度为n的输入序列分成两个长度为n/2的子序列；
2. 对这两个子序列分别采用归并排序；
3. 将两个排序好的子序列合并成一个最终的排序序列。

## 算法分析
归并排序是一种稳定的排序方法。和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，
因为始终都是$O(n\log(n))$的时间复杂度。代价是需要额外的内存空间$O(n)$。

1. 归并排序法，$n$项数据一般需要约$\log_2(n)$ 次处理，每次处理的时间复杂度为$O(n)$，
所以合并排序法的最佳情况、最差情况及平均情况**时间复杂度为$O(n\log(n))$**。
2. 由于在排序过程中需要一个与数列大小同样的额外空间，故其**空间复杂度为$O(n)$**。
3. 归并排序是一个**稳定排序方式**。

## 动图演示
![](https://github.com/pchen12567/picture_store/blob/master/Algorithm/mergeSort_01.gif?raw=true)
![](https://github.com/pchen12567/picture_store/blob/master/Algorithm/mergeSort_02.gif?raw=true)

## 过程分解图
![](https://github.com/pchen12567/picture_store/blob/master/Algorithm/mergeSort_03.jpg?raw=true)
