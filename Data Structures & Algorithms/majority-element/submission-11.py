import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        app = nums[0]
        cnt = nums.count(app)
        rnd = 0
        while cnt <= (len(nums) / 2):
            rnd = random.randint(0, len(nums) - 1)
            cnt = nums.count(nums[rnd])
        return nums[rnd]