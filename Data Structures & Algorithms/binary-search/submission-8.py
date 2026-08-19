class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        l,r = 0, len(nums) - 1
        if len(nums) == 1:
            return 0 if nums[-1] == target else answer

        while l <= r:
            mid = (l + r) // 2
            x = nums[mid]
            if x == target:
                return mid
            elif target > x:
                l = mid + 1
            else:
                r = mid - 1
        
        return answer
