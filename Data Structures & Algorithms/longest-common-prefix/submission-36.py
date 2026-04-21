from functools import reduce
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minii = min(strs, key=lambda x: len(x))
        hol = [all([minii[:i] in item for item in strs]) for i in range(1, len(minii) + 1)]
        allss = sorted([minii[:i] for i in range(1, len(minii)+1)  if all([minii[:i] in item for item in strs])], reverse=True)
        return allss[0] if len(allss) else ""

