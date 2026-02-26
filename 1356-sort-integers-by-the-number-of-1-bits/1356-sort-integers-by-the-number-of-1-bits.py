class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: [self.countBits(x), x])
        return arr

    def countBits(self, num):
        count = 0
        while num:
            count += (num & 1)
            num >>= 1
        return count