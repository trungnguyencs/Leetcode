class NumArray:
    
    # sqrt decomposition
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.blockSize = ceil(len(nums)**0.5)
        self.blockSum = [0]*self.blockSize
        for i, num in enumerate(nums):
            self.blockSum[i//self.blockSize] += num
                        
    # O(1) time
    def update(self, index: int, val: int) -> None:
        self.blockSum[index // self.blockSize] += val - self.nums[index]
        self.nums[index] = val
        
    # O(sqrt(n)) time
    def sumRange(self, left: int, right: int) -> int:
        idxLeft, offsetLeft = divmod(left, self.blockSize)
        idxRight, offsetRight = divmod(right, self.blockSize)
        return sum(self.blockSum[idxLeft: idxRight + 1])\
            - sum(self.nums[idxLeft*self.blockSize: idxLeft*self.blockSize + offsetLeft])\
            - sum(self.nums[idxRight*self.blockSize + offsetRight + 1: (idxRight + 1)*self.blockSize])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)