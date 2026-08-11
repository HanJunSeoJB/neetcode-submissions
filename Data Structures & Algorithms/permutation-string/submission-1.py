class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)

        if l1 > l2:
            return False
        
        ch_a, ch_b = [0] * 26, [0] * 26

        for i in range(l1):
            ch_a[ord(s1[i]) - ord('a')] += 1
            ch_b[ord(s2[i]) - ord('a')] += 1

        if ch_a == ch_b:
            return True
        
        for i in range(l1, l2):
            ch_b[ord(s2[i]) - ord('a')] += 1
            ch_b[ord(s2[i - l1]) - ord('a')] -= 1

            if ch_a == ch_b:
                return True
        return False