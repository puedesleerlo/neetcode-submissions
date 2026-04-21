from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anan = defaultdict(list)
        seen = ("".join((sorted(str_i))) for str_i in strs)
        for seen_i, str_i in zip(seen, strs):
                anan[seen_i].append(str_i)
        return list(anan.values())

            
            