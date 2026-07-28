from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = deque()
        answer = 0
        for c in s:
            if c in output:
                while c in output:
                    output.popleft()
            output.append(c)
            answer = max(answer, len(output))
        return answer