class MyCalendarTwo:

    def __init__(self):
        self.time = []

    def book(self, startTime: int, endTime: int) -> bool:
        insort(self.time,(startTime,0,1))
        insort(self.time,(endTime,-1,-1))
        cur = 0
        for y,tempo,tf in self.time:
            cur+=tf
            if cur == 3:
                self.time.remove((startTime,0,1))
                self.time.remove((endTime,-1,-1))
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)