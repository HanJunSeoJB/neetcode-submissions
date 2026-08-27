from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # 순서가 유지되는 해시 맵 (내부적으로 이중 연결 리스트 구현됨)
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # 데이터를 조회했으므로 '가장 최신(맨 뒤)' 상태로 순서를 옮겨줍니다.
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 이미 있는 키라면 값을 업데이트하고 맨 뒤로 보냅니다.
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # 새로운 키라면 일단 추가합니다.
            self.cache[key] = value
            
            # 용량을 초과했다면 가장 오래된(맨 앞, last=False) 데이터를 삭제합니다.
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)