class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z, ans = x^y, 0
        while z > 0:
            ans += z % 2
            z //= 2
        return ans
    