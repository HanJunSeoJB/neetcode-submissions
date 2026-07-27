class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        # heights.sort()
        n = len(heights)
        l, r = 0, len(heights) - 1

        def get_area(l, r):
            return abs(l - r) * min(heights[l], heights[r])

        while l < r:
            answer = max(answer, get_area(l, r))
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        
        return answer