class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 荷兰国旗问题
        # Solution: Tow Pointer
        # Time: 4ms
        position_zero = 0
        position_two = len(nums) - 1
        i = 0
        while i <= position_two:
            if nums[i] == 0:
                nums[i], nums[position_zero] = nums[position_zero], nums[i]
                position_zero += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[position_two] = nums[position_two], nums[i]
                position_two -= 1
            else:
                i += 1
