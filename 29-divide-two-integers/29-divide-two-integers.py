class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == -2**31 and b == -1: return 2**31 - 1
        A, B, ans = abs(a), abs(b), 0
        while A >= B:
            tmp, i = B, 1
            while (tmp << 1) <= A:
                tmp <<= 1
                i <<= 1
            A -= tmp
            ans += i
        return ans if (a > 0) == (b > 0) else -ans