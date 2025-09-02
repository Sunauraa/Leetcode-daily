class TimeMap:

    def __init__(self):
        self.timeline = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        m = defaultdict(str)
        if self.timeline:
            m = self.timeline[-1][1].copy()
        m[key] = value
        self.timeline.append( (timestamp, m.copy()) )

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeline:
            return ''
        l,r = 0, len(self.timeline) - 1
        findm = defaultdict(str)
        while l <= r:
            mid = (l+r)
            if self.timeline[mid][0] > timestamp:
                r = mid - 1
            else:
                findm = self.timeline[mid][1]
                l = mid + 1
        return findm[key]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)