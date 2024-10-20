class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # The first digit is always "0" regardless of n
        # The middle digit is always 1
        # If k < mid, one could reduce the problem to n-1 which is half the size
        # Otherwise, focus on the other half by reversing the position and "0"/"1"
        length = 2**n - 1
        if k == 1: return '0'
        if k == length//2: return '1'
        if k < length//2: return self.findKthBit(n - 1, k)
        return self.flip(self.findKthBit(n - 1, length + 1 - k))
    
    def flip(self, bit):
        return '0' if bit == '1' else '1'