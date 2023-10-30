class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: [self.countOnes(x), x])
        
    def countOnes(self, num):
        count = 0
        while num:
            count += (num & 1)
            num >>= 1
        return count