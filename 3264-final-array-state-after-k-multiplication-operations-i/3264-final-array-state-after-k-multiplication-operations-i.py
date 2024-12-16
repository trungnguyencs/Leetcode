class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ans = [0]*len(nums)
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            num, i = heappop(heap)
            heappush(heap, (num * multiplier, i))
        for num, i in heap:
            ans[i] = num
        return ans