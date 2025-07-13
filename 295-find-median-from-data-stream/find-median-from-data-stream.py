class MedianFinder:

    def __init__(self):
        self.q = []

    def addNum(self, num: int) -> None:
        pos = bisect.bisect_left( self.q, num )
        self.q.insert(pos, num)

    def findMedian(self) -> float:
        n = len(self.q)
        if len(self.q)%2:
            return self.q[n//2]*1.0
        else:
            return (self.q[n//2] + self.q[n//2-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()