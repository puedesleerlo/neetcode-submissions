class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        pasos = 0
        index = 0
        while index <= right:
            num = nums[index]
            if num == 0:
                nums[index] = nums[left]
                nums[left] = 0
                left += 1
                index += 1
            elif num == 1:
                index += 1
            elif num == 2:
                nums[index] = nums[right]
                nums[right] = 2
                right -= 1

            

            