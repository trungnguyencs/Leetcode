class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)
        visited = set()
        ans = 0
        while heap:
            num, i = heappop(heap)
            if i in visited: continue
            ans += num
            visited.update([i, i-1, i+1])
        return ans      