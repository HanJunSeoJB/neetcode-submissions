class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # daily = [0] * len(temperatures)
        d = []
        tp = list(reversed(temperatures))
        n = len(tp)
        # print(tp)
        for idx, tk in enumerate(tp):
            while len(d) and temperatures[d[-1]] <= tk:
                d.pop()
            if len(d) > 0:
                result[n-idx-1] = d[-1] - (n-idx-1)
                
            d.append(n-idx-1)
 
            # print(d)
        return result

