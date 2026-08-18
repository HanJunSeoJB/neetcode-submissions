class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tmp = []
        answer = 0

        st_p = [(i, x) for i, x in enumerate(position)]
        st_p.sort(key=lambda x: x[1], reverse=True)

        for idx, p in st_p:
            tmp.append((target - p) / speed[idx])

        # print(tmp)
        max_time = 0
        
        for t in tmp:
            if t > max_time:
                answer += 1
                max_time = t
                
        return answer