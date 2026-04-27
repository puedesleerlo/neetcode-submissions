class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        old_cnt = 0
        for num in nums:
            if num - 1 not in nums:
                length = 0
                cc = num
                while cc in nums:
                    length += 1
                    cc += 1
                if length > old_cnt:
                    old_cnt = length
        return old_cnt            
            