class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonZeroes = {i: num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, val in self.nonZeroes.items(): #further optimization: loop on the vec with fewer non-zeroes
            if i in vec.nonZeroes:
                ans += val * vec.nonZeroes[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)