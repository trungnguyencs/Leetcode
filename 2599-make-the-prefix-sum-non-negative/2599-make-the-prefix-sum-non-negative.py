class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        curSum = ops = 0
        heap = []
        for num in nums:
            curSum += num
            if num < 0:
                heappush(heap, num)
            if curSum < 0:
                curSum -= heappop(heap)
                ops += 1
        return ops