class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = b = 0
        i = 1
        while n:
            d = n % 10
            n //= 10
            if d == 0:
                a += 1 * i
                b += 9 * i
                n -= 1
            elif d == 1 and n > 0:
                a += 2 * i
                b += 9 * i
                n -= 1
            else:
                a += i
                b += (d - 1) * i
            i *= 10
        return [a, b]