from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        answer = []
        for ke, v in c.items():
            answer.append([ke, v])
        answer.sort(key=lambda x: -x[1])
        print(answer)
        return [row[0] for row in answer[:k]]
        