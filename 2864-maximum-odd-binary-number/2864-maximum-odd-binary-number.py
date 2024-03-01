class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        l = 0
        for r, ch in enumerate(s):
            if ch == '1':
                s[l], s[r] = s[r], s[l]
                l += 1
        s[l-1], s[-1] = s[-1], s[l-1]
        return ''.join(s)