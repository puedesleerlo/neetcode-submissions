class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hastable = {}
        for num in nums:
            if num in hastable:
                hastable[num] += 1
            else:
                hastable[num] = 1
        # reversed_hastable = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        for ii, obj in hastable.items():
            buckets[obj].append(ii)
        clean = [it for i in range(len(buckets)-1, 0, -1) if len(buckets[i]) > 0 for it in buckets[i]]

        return clean[:k]