class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            elif heap[0] < num:
                heapreplace(heap, num)
        return heap[0]