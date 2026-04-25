class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n

        # forward pass: out[i] = product of everything to the left
        for i in range(1, n):
            out[i] = out[i-1] * nums[i-1]

        # backward pass: multiply in product of everything to the right
        right = 1
        for i in range(n-1, -1, -1):
            out[i] *= right
            right *= nums[i]

        return out