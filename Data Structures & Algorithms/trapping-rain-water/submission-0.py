class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, lp, rp = 0, len(height)-1, height[0], height[len(height)-1]
        answer = 0

        while l < r:
            if lp < rp:
                l += 1
                lp = max(lp, height[l])
                answer += lp - height[l]
            else:
                r -= 1
                rp = max(rp, height[r])
                answer += rp - height[r]
        
        return answer
            
