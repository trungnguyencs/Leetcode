class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        l, r = 1, num//2 + 1
        while l < r:
            m = (l + r)//2
            if m**2 <= num < (m + 1)**2:
                return m**2 == num
            if m**2 < num:
                l = m + 1
            else:
                r = m
                        