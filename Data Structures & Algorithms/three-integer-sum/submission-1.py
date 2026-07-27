class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        t = 0
        while t < n and nums[t] <= 0:
            answer.append(t)
            t += 1
        
        result = []
        for ta in answer:
            if ta > 0 and nums[ta-1] == nums[ta]:
                continue

            l, r = ta+1, n-1
            while l < r:
                total = nums[ta] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[ta], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                if total > 0:
                    r -= 1
                    continue
                if total < 0:
                    l += 1
                    continue

        return result