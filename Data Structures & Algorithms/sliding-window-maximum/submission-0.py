import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        answer = []
        
        for r in range(len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))

            if r < k - 1:
                continue

            while max_heap[0][1] < r - k + 1:
                heapq.heappop(max_heap)    

            answer.append(-max_heap[0][0])
        return answer
 