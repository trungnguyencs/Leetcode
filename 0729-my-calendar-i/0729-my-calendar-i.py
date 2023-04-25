from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        self.dic = SortedDict()

    # def book(self, start: int, end: int) -> bool:
    #     keys = self.dic.keys()
    #     if keys:
    #         r = self.dic.bisect_right(start)
    #         if r != 0:
    #             floorKey = self.dic[keys[r-1]]
    #             if floorKey > start: return False
    #         l = self.dic.bisect_left(start)
    #         if l != len(keys):
    #             ceilKey = keys[l]
    #             if end > ceilKey: return False
    #     self.dic[start] = end
    #     return True
        
    def book(self, start: int, end: int) -> bool:
        keys = self.dic.keys()
        if keys:
            i = self.dic.bisect_right(start)
            if i != 0:
                floorKey = self.dic[keys[i-1]]
                if floorKey > start: return False
            if i == len(keys) and start == keys[-1]: i -= 1 # do this equivalent to bisect_left() to save time
            if i != len(keys):
                ceilKey = keys[i]
                if end > ceilKey: return False
        self.dic[start] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)