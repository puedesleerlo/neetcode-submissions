class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        pasos = 0
        index = 0
        while pasos < len(nums):
            num = nums[index]
            if num == 0 and index >= left:
                nums[index] = nums[left]
                nums[left] = 0
                left += 1
                index += 1
            elif num == 1:
                index += 1
            elif num == 2 and index <= right:
                nums[index] = nums[right]
                nums[right] = 2
                right -= 1
            pasos += 1


            

            