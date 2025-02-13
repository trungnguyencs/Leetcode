class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        heapify(nums)
        while nums[0] < k:
            x, y = heappop(nums), heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            ops += 1
        return ops