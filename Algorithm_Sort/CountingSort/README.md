# Counting Sort 计数排序
计数排序要求输入数据的范围在$[0,N-1]$之间，则可以开辟一个大小为$N$的数组空间，将输入的数据值转化为键存储在该数组空间中，
数组中的元素为该元素出现的个数。它是一种线性时间复杂度的排序。

计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

## 算法描述
1. 找出待排序的数组中最大和最小的元素；
2. 统计数组中每个值为$i$的元素出现的次数，存入数组$C$(bucket)的第$i$项；
3. 对所有的计数累加（从$C$中的第一个元素开始，每一项和前一项相加）；
4. 反向填充目标数组：将每个元素$i$放在新数组的第$C(i)$项，每放一个元素就将$C(i)$减去1。

## 算法分析
计数排序是一个稳定的排序算法。当输入的元素是$n$个0到$k$之间的整数时，时间复杂度是$O(n+k)$，空间复杂度也是$O(n+k)$，
其排序速度快于任何比较排序算法。当$k$不是很大并且序列比较集中时，计数排序是一个很有效的排序算法。
1. 时间复杂度：$O(n + k)$。
2. 空间复杂度：$O(k)$。
3. 稳定性：稳定。

## 动图演示
![](https://github.com/pchen12567/picture_store/blob/master/Algorithm/countingSort_01.gif?raw=true)
