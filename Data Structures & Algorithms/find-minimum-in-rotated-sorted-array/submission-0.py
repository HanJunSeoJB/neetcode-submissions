class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        answer = float('inf')
        while l <= r:
            mid = (l + r) // 2
            x = nums[mid]
            rv = nums[r]
            lv = nums[l]

            if x > rv:
                l = mid + 1
            else:
                answer = min(answer, x)
                r = mid - 1
            
        return answer
