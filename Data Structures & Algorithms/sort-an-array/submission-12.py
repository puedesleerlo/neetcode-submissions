class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       def merge(arr, L, M, R):
        Left, Right = arr[L:M+1], arr[M+1:R+1]
        i, j, k = L, 0, 0

        while j < len(Left) and k < len(Right): # para evitar out of bounds
            if Left[j] <= Right[k]:
                arr[i] = Left[j]
                j += 1
            else:
                arr[i] = Right[k]
                k += 1
            i += 1
        while j < len(Left):
            nums[i] = Left[j]
            j += 1
            i += 1
        
        while k < len(Right):
            nums[i] = Right[k]
            k += 1
            i += 1
        
            

        
       def mergeSort(arr, l, r):
        if l == r:
            return arr
        m = (l + r)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
        return arr
       return mergeSort(nums, 0, len(nums) - 1)
            
                

