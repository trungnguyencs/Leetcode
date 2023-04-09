class Solution:
    def findComplement(self, num: int) -> int:
        ans = i = 0
        while num:
            lastBit = num & 1
            ans |= (1 - lastBit) << i
            num >>= 1
            i += 1
        return ans