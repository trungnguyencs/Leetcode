class Solution:
    # Solution 1
    # def bitwiseComplement(self, n: int) -> int:
    #     if n == 0: return 1
    #     ans = bitCount = 0
    #     while n:
    #         ans += 2**bitCount*(1 - n % 2)
    #         n //= 2
    #         bitCount += 1
    #     return ans
    
    # Solution 2
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        bitCount, temp = 0, n
        while temp > 0:
            temp >>= 1
            bitCount += 1
        return 2**bitCount - 1 - n