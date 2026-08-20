class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r= 0, len(nums) - 1

        answer = -1

        while l <= r:
            mid = (l + r) // 2
            x = nums[mid]
            lv = nums[l]
            rv = nums[r]

            if x == target:
                return mid
            elif x > rv:
                if target < x and target >= lv:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if target <= rv and target > x:
                    l = mid + 1
                else:
                    r = mid - 1

        return answer