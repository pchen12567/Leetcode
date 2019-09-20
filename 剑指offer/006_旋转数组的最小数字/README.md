## 题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

## 思路
二分法

mid = (left + right) // 2

需要考虑三种情况：
1. array[mid] > array[right]:<br>
    此时最小数字一定在mid的右边。<br>
    left = mid + 1
2. array[mid] < array[right]:<br>
    此时最小数字一定就是array[mid]或者在mid的左边。<br>
    right = mid
3. array[mid] = array[right]:<br>
    此时最小数字不好判断在mid左边还是右边，这时只好一个一个试。<br>
    right -= 1