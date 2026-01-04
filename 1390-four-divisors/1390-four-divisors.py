class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(self.getSumDivisors(num) for num in nums)

    def getSumDivisors(self, num):
        divisors = set()
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.update([i, num//i])
            if len(divisors) > 4: break
        return sum(divisors) if len(divisors) == 4 else 0