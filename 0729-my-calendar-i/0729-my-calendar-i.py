from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        self.dic = SortedDict()

    def book(self, start: int, end: int) -> bool:
        keys = self.dic.keys()
        if keys:
            l = self.dic.bisect_left(start)
            if l != len(keys):
                if end > keys[l]: return False
            r = self.dic.bisect_right(start)
            if r != 0:
                if self.dic[keys[r-1]] > start: return False
        self.dic[start] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)