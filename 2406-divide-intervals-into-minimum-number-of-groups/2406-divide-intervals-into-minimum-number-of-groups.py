class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for s, e in intervals:            
            if not heap or s <= heap[0]:
                heappush(heap, e)
            else:
                heapreplace(heap, e)
        return len(heap) 