class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0: return '-' + self.convertToBase7(-num)
        ans, base = 0, 1
        while num > 0:
            ans += (num % 7) * base
            num //= 7
            base *= 10
        return str(ans)