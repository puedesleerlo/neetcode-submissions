class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        old_cnt = 0
        seen = set()
        for i in range(len(nums)):
            indd = i
            cnt = 1
            if nums[indd] in seen:
                continue  
            while True:
                fo = nums[indd] + 1
                try:
                    indd = nums.index(fo)
                    seen.add(nums[indd])
                    cnt += 1
                except:
                    break
            if cnt > old_cnt:
                old_cnt = cnt
        return old_cnt            
            