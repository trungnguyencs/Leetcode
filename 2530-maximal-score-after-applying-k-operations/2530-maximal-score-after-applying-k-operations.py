class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        heap = [-num for num in nums]
        heapify(heap)
        for _ in range(k):
            num = -heappop(heap)
            ans += num
            heappush(heap, -math.ceil(num/3))
        return ans