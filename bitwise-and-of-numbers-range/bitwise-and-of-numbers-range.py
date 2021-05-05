class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        # only the most significant overlapping bits count
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return left << i