class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anan = {}
        for i, str_i in enumerate(strs):
            seen = "".join((sorted(str_i)))
            if seen in anan:
                anan[seen].append(str_i)
            else:
                anan[seen] = [str_i]
        return list(anan.values())

            
            