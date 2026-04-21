class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valll = nums.count(val)
        cnt = 0
        while cnt < valll:
            nums.remove(val)
            cnt += 1
        return len(nums)