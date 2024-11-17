class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = [(0, -1)]
        curSum = 0
        ans = float('inf')
        for i, num in enumerate(nums):
            curSum += num
            while heap and curSum - heap[0][0] >= k:
                _, j = heappop(heap) #important observation: if current end satisfies, later ends cannot be shorter, so it's safe to pop here
                ans = min(ans, i - j)
            heappush(heap, (curSum, i))
        return ans if ans != float('inf') else -1