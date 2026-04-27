class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        old_cnt = 0
        numSet = set(nums)
        for num in nums:
            if num - 1 not in numSet:
                length = 0
                cc = num
                while cc in numSet:
                    length += 1
                    cc += 1
                if length > old_cnt:
                    old_cnt = length
        return old_cnt            
            