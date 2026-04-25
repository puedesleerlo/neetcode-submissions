class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        for i in range(len(nums)):
            # El segundo número multiplica al arreglo 0 , 2 en adelante
            # El tercer número multiplica al arreglo 0, 1, y 3 en adelante
            for j in range(len(nums)):
                if i != j:
                    arr[i] = arr[i]*nums[j]
        return arr