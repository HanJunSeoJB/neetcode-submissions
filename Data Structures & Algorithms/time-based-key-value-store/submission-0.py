class TimeMap:

    def __init__(self):
        self.bucket = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.bucket:
            self.bucket[key] = []
        self.bucket[key].append((value, timestamp))
        # print(self.bucket)

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.bucket:
            return ""

        l, r = 0, len(self.bucket[key]) - 1
        answer = ""
        while l <= r:
            mid = (l + r) // 2
            x, time = self.bucket[key][mid]

            if time == timestamp:
                return x

            elif time < timestamp:
                answer = x
                l = mid + 1
            else:
                r = mid - 1
        return answer