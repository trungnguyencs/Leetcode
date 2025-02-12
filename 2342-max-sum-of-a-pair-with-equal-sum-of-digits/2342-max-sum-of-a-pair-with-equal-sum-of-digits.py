class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        dic = defaultdict(list)
        for num in nums:
            sumDigits = self.getDigitSum(num)
            heap = dic[sumDigits]
            heappush(heap, num)
            if len(dic[sumDigits]) > 2:
                heappop(heap)
            if len(heap) == 2:
                ans = max(ans, sum(heap))
        return ans

    def getDigitSum(self, num):
        sumDigits = 0
        while num:
            sumDigits += num % 10
            num //= 10
        return sumDigits