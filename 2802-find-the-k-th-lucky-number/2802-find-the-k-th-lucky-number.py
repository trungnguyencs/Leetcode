class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        s = bin(k + 1)[3:]
        return s.replace('0', '4').replace('1', '7')