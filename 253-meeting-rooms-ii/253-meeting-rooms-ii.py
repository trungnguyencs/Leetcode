class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = float('-inf')
        heap = []
        for s, e in intervals:
            while heap and s >= heap[0]:
                heappop(heap)
            heappush(heap, e)
            ans = max(ans, len(heap))
        return ans