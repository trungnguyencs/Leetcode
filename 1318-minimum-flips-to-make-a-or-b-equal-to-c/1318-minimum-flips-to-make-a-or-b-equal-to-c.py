class Solution:
    def minFlips(self, num1: int, num2: int, target: int) -> int:
        count = 0
        while num1 or num2 or target:
            b1, b2, b3 = num1 & 1, num2 & 1, target & 1
            if b3 == 0:
                if b1 == b2 == 1:
                    count += 2
                elif b1 == 1 or b2 == 1:
                    count += 1
            elif b1 == b2 == 0:
                count += 1
            num1 >>= 1
            num2 >>= 1
            target >>= 1
        return count