class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {i: num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(self.dic[i] * vec.dic[i] for i in self.dic if i in vec.dic)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)