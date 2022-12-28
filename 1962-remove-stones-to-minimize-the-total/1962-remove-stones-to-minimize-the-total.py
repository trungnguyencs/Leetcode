class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapify(heap)
        for _ in range(k):
            largest = -heappop(heap)
            heappush(heap, -(largest - largest//2))
        return -sum(heap)