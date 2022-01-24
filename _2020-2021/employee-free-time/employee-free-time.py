"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedules: '[[Interval]]') -> '[Interval]':
        heap = [[schedule[0].start, schedule[0].end, 0, id] for id, schedule in enumerate(schedules)]
        heapify(heap)
        _, lastEnd, _, _ = heap[0]
        ans = []
        while heap:
            curStart, curEnd, i, id = heappop(heap)
            if curStart > lastEnd:
                ans.append(Interval(lastEnd, curStart))
            if i < len(schedules[id]) - 1:
                heappush(heap, [schedules[id][i+1].start, schedules[id][i+1].end, i+1, id])
            lastEnd = max(lastEnd, curEnd)
        return ans