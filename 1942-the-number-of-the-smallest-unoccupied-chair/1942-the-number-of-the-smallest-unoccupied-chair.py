class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arr = [(time, person) for person, time in enumerate(times)]
        arr.sort()
        heap = []
        chairs = []
        for (s, e), person in arr:
            while heap and s >= heap[0][0]:
                _, chair = heappop(heap)
                heappush(chairs, chair)
            chair = len(heap) if len(chairs) == 0 else heappop(chairs) 
            if person == targetFriend: return chair
            heappush(heap, (e, chair))