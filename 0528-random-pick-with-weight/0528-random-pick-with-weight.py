class Solution:

    def __init__(self, w: List[int]):
        self.arr = w
        for i in range(1, len(self.arr)):
            self.arr[i] += self.arr[i-1]
        self.maxVal = self.arr[-1]

    def pickIndex(self) -> int:
        num = randint(1, self.maxVal)
        return bisect_left(self.arr, num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()