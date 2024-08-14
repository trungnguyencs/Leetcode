class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = []
        tmp = n
        while tmp:
            digits.append(tmp % 10)
            tmp //= 10
        return sum(d**len(digits) for d in digits) == n    