class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.store = defaultdict(list)
        for i in range(len(arr)):
            self.store[arr[i]].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for i in range(10):
            rand = random.randint(left,right)
            check = self.arr[rand]
            l = bisect.bisect_left(self.store[check], left)
            r = bisect.bisect_right(self.store[check],right)
            if r - l >= threshold:
                return check
        return -1
              


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)