class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == -2**31 and b == -1: return 2**31 - 1
        A, B, ans = abs(a), abs(b), 0
        while A >= B:
            temp, i = B, 1
            while A >= (temp << 1):
                temp <<= 1
                i <<= 1
            A -= temp
            ans += i
        return ans if (a > 0) == (b > 0) else -ans 