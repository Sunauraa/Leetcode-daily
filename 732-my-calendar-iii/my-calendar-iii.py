class MyCalendarThree:

    def __init__(self):
        self.time = []

    def book(self, startTime: int, endTime: int) -> int:
        insort(self.time,(startTime,1,1))
        insort(self.time,(endTime,-1,-1))
        cur = 0
        ans = 0
        for y,tempo,tf in self.time:
            cur+=tf
            ans = max(ans,cur)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)