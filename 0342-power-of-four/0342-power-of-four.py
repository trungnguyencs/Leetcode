class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        #recursive solution is trivial
        #a number is power of 4 if it's a power of 2 and the 1 bit is at odd index (i.e. 1, 3, 5, ...)
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num   