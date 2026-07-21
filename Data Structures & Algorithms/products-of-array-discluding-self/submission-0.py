class Solution:
    def mul(self, nums: List[int]) -> int:
        answer = 1
        n = len(nums)
        # print(nums)
        if n == 0: return answer
        for i in range(n):
            answer *= nums[i]
        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [0] * n
        for i in range(n):
            answer[i] = self.mul(nums[:i]) * self.mul(nums[i+1:])
        return answer