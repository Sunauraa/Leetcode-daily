class MyCalendar:

    def __init__(self):
        self.time = []

    def book(self, startTime: int, endTime: int) -> bool:
        for l,r in self.time:
            if not( startTime >= r or endTime <= l ):
                return False
        insort(self.time,(startTime,endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)