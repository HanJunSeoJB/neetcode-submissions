class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        n = len(s)
        answer = 0
        max_val = 0

        for i in range(n):
            count[s[i]] = 1 + count.get(s[i], 0)
            max_val = max(max_val, count[s[i]])

            if (i - l + 1) - max_val > k:
                count[s[l]] -= 1
                l += 1

        return (i - l + 1)
