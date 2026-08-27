class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        last, first = nums[0], nums[0]

        while 1:
            last = nums[last]
            first = nums[nums[first]]

            if last == first:
                break

        wtf = nums[0]

        while wtf != last:
            wtf = nums[wtf]
            last = nums[last]

        return wtf