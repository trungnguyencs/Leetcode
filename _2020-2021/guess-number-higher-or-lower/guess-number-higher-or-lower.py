# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n+1
        while l < r:
            m = (l + r)//2
            if guess(m) == 0: return m
            if guess(m) == -1:
                r = m
            else:
                l = m + 1
        return l
            