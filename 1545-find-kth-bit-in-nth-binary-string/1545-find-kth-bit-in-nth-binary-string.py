class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1
        if k == 1: return '0'
        if k == length//2: return '1'
        if k > length//2: return self.flip(self.findKthBit(n - 1, length + 1 - k))
        return self.findKthBit(n - 1, k)
    
    def flip(self, bit):
        return '0' if bit == '1' else '1'