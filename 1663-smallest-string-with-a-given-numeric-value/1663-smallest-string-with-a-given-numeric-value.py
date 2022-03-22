class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # k - 26*zCount >= n - zCount
        # k - n >= 25*zCount
        zCount = (k - n)//25
        if zCount == n: return 'z'*zCount
        aCount = n - zCount - 1
        soleDigit = chr(ord('a') + k - 26*zCount - aCount - 1)
        return 'a'*aCount + soleDigit + 'z'*zCount