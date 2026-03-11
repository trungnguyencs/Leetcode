class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        ans = i = 0
        while n:
            b = 1 - (n & 1)
            ans += (b << i)
            i += 1
            n >>= 1
        return ans