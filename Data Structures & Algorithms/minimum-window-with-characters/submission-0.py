from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ch_t = defaultdict(int)
        ch_w = defaultdict(int)

        for i in range(len(t)):
            ch_t[t[i]] += 1
        
        l = 0

        need = len(ch_t)
        have = 0

        res, res_len = [-1, -1], float("inf")

        for r in range(len(s)):
            ch_w[s[r]] += 1
            if s[r] in ch_t and ch_w[s[r]] == ch_t[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = [l, r]

                x = s[l]
                ch_w[x] -= 1

                if x in ch_t and ch_w[x] < ch_t[x]:
                    have -= 1
                

                l += 1



        return s[res[0] : res[1] + 1] if res_len != float("inf") else ""
