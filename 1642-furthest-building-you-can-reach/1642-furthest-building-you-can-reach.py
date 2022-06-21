class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # greedy solution
        heap = []
        for i in range(len(heights) - 1):
            d = heights[i+1] - heights[i]
            if d <= 0: continue
            heappush(heap, d)
            if ladders > 0:
                ladders -=1
                continue
            if ladders == 0 and bricks < heap[0]: return i
            bricks -= heappop(heap)
        return len(heights) - 1

#     # dp solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         self.heights = heights
#         return self.dp(0, bricks, ladders)
    
#     @cache
#     def dp(self, i, bricks, ladders):
#         if i == len(self.heights) - 1: return i
#         d = self.heights[i+1] - self.heights[i]
#         if d <= 0: return self.dp(i + 1, bricks, ladders)
#         if bricks < d and ladders == 0: return i
#         ret = i
#         if bricks >= d:
#             ret = max(ret, self.dp(i + 1, bricks - d, ladders))
#         if ladders > 0:
#             ret = max(ret, self.dp(i + 1, bricks, ladders - 1))
#         return ret