class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = tuple(sorted(s))
        s2 = tuple(sorted(t))
        return s1 == s2