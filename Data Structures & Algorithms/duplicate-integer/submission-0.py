from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = Counter(nums)
        return any(x > 1 for x in s.values())