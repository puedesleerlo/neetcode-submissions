class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        arr[0] = nums[0]
        arr_r = [1] * len(nums)
        def_ar = [1] * len(nums)
        lv = len(nums) - 1
        arr_r[lv] = nums[lv]
        for i in range(1, len(nums)):
            arr[i] = arr[i-1]*nums[i]
            arr_r[lv - i] = arr_r[lv - i + 1]*nums[lv - i]
            # def_ar[i] = arr[i-1]*arr_r[i+1]
            # print(nums[i], arr[i-1], arr_r[i + 1], i + 1)
        print(arr, arr_r)
        def_ar[0] = arr_r[1]
        def_ar[len(nums) - 1] = arr[len(nums) - 2]    
        for i in range(1, len(nums) - 1):
            def_ar[i] = arr[i-1]*arr_r[i+1]    
        return def_ar