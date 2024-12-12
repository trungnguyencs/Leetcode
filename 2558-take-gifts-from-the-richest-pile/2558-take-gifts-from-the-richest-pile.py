class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-num for num in gifts]
        heapify(heap)
        for _ in range(k):
            num = -heappop(heap)
            heappush(heap, int(-math.sqrt(num)))
        return -sum(heap)