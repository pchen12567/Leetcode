# 十大经典排序算法

## 算法分类
十种常见排序算法可以分为两大类：

1. **比较类排序**：通过比较来决定元素间的相对次序，由于其时间复杂度不能突破$O(n\log(n))$，因此也称为非线性时间比较类排序。
2. **非比较类排序**：不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序。
![](https://github.com/pchen12567/picture_store/blob/master/Algorithm/algorithm_sort_02.png?raw=true) 

## 算法复杂度
![](https://github.com/pchen12567/picture_store/blob/master/Algorithm/algorithm_sort_01.jpeg?raw=true)

## 相关概念
- **n**：数据规模。
- **k**："桶"的个数。
- **In-place**：占用常数内存，不占用额外内存。
- **Out-place**：占用额外内存。
- **稳定**：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
- **不稳定**：如果a原本在b的前面，而a=b，排序之后 a可能会出现在b的后面。
- **时间复杂度**：对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。
- **空间复杂度**：是指算法在计算机内执行时所需存储空间的度量，它也是数据规模n的函数。

## 算法详解
- [冒泡排序: Bubble Sort](https://github.com/pchen12567/Leetcode/tree/master/Algorithm_Sort/BubbleSort)
- [选择排序: Selection Sort](https://github.com/pchen12567/Leetcode/tree/master/Algorithm_Sort/SelectionSort)
- [归并排序: Merge Sort](https://github.com/pchen12567/Leetcode/tree/master/Algorithm_Sort/MergeSort)