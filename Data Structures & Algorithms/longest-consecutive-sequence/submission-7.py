class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        old_cnt = 0
        for i in range(len(nums)):
            indd = i
            cnt = 1
            while True:
                fo = nums[indd] + 1
                print(fo)
                try:
                    indd = nums.index(fo)
                    cnt += 1
                except:
                    break
            if cnt > old_cnt:
                old_cnt = cnt
        return old_cnt            
            