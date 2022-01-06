class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, s, e in trips:
            events.extend([[s, 1, num], [e, 0, num]]) # 1: start, 0: end
        for time, event, num in sorted(events):
            capacity += num if event == 0 else -num
            if capacity < 0: return False
        return True