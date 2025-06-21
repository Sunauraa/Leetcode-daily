class LRUCache:
    arr = []
    capacity = 0
    m = defaultdict(int)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = []
        m = defaultdict(int)

    def get(self, key: int) -> int:
        m = self.m
        arr = self.arr
        if key in arr:
            arr.remove(key)
            arr.append(key)
            #  print(arr)
            return m[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        arr = self.arr
        capacity = self.capacity
        m = self.m
        if key in arr:
            arr.remove(key)
        while len(arr) >= capacity:
            arr.remove(arr[0])
        arr.append(key)
        m[key] = value
        #print(arr)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)