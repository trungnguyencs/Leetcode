class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # assuming the 2 numbers are a and b
        # xor all of nums we will have xorAll = a ^ b
        # because a != b there will at least one 1 bit in xorAll 
        # xor all the numbers having that same 1 bit we found a
        # find b: a ^ b = xorAll => b = a ^ xorAll
        xorAll = 0
        for num in nums:
            xorAll ^= num
        bitOne = 1
        while bitOne & xorAll == 0:
            bitOne <<= 1
        a = 0
        for num in nums:
            if num & bitOne:
                a ^= num
        return a, a ^ xorAll