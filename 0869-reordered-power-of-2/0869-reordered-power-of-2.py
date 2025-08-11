class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powersOfTwo = [2**x for x in range(31)]
        counterN = Counter(str(n))
        for powerOfTwo in powersOfTwo:
            if Counter(str(powerOfTwo)) == counterN:
                return True
        return False