class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hastable = {}
        for num in nums:
            if num in hastable:
                hastable[num] += 1
            else:
                hastable[num] = 1
        print(hastable)
        reversed_hastable = {}
        for ii, obj in hastable.items():
            if obj in reversed_hastable:
                reversed_hastable[obj].append(ii)
            else:
                reversed_hastable[obj] = [ii]

        k_items = sorted(reversed_hastable.items(), key=lambda x: x[0], reverse = True)
        sortable = [ i  for it in k_items for i in it[1]]
        print(sortable)
        return sortable[:k]