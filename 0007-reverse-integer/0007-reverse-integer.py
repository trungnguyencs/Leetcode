class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: return -self.reverse(-x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        return ans if -2**31 <= ans <= 2**31 - 1 else 0