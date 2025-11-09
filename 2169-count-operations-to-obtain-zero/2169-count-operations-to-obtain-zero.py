class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        a, b = max(num1, num2), min(num1, num2)
        ops = 0
        while a > 0 and b > 0:
            ops += a // b
            a, b = b, a % b
        return ops