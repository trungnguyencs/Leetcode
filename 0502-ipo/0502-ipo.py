class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        heap = []
        sortedByCapital = sorted(zip(capitals, profits))
        capitals = [c for c, _ in sortedByCapital]
        profits = [p for _, p in sortedByCapital]
        i = 0
        while k > 0:
            while i < len(capitals) and w >= capitals[i]:
                heappush(heap, -profits[i])
                i += 1
            if not heap or heap[0] > 0: # negative gain
                return w
            w -= heappop(heap)
            k -= 1
        return w 