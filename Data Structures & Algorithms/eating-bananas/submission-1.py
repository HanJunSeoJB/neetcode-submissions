import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        answer = 0

        l, r = 1, max(piles)
        def cal(a):
            return sum([math.ceil(x / a) for x in piles])
        # print(cal(1))
        while l <= r:
            mid = (l + r) // 2
            total = cal(mid)
            if total <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l
