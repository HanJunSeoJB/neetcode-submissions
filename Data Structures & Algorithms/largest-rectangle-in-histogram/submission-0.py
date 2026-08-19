class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        answer = 0
        heights.append(0)
        for idh, h in enumerate(heights):
            while len(stack) and stack[-1][1] > h:
                idx, x = stack.pop()
                answer = max(answer, ((idh-stack[-1][0]-1 if len(stack) else idh) * x))
            stack.append((idh, h))

        return answer