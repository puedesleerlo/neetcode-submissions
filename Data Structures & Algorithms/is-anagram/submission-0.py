class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st1 = sorted(s)
        st2 = sorted(t)
        return st1 == st2