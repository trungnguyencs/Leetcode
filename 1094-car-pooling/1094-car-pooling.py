class Solution:
    # def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    #     events = []
    #     for num, s, e in trips:
    #         events.extend([[s, 1, num], [e, 0, num]]) # 1: start, 0: end
    #     for time, event, num in sorted(events):
    #         capacity += num if event == 0 else -num
    #         if capacity < 0: return False
    #     return True
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))
        heap = []
        for num, s, e in trips:
            while heap and heap[0][0] <= s:
                _, _, releasedNum = heappop(heap)
                capacity += releasedNum
            if capacity < num:
                return False
            capacity -= num
            heappush(heap, (e, s, num)) # what ends first is on top of heap
        return True