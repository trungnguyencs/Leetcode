class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        ans = 0
        for s, e in intervals:
            while heap and heap[0] <= s:
                heappop(heap)
            heappush(heap, e)
            ans = max(ans, len(heap))
        return ans