class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            if self.isSymmetric(num):
                ans += 1
        return ans

    def isSymmetric(self, num):
        digits = [int(d) for d in str(num)]
        n = len(digits)
        if n % 2 == 1: return False
        return sum(digits[:n//2]) == sum(digits[n//2:])