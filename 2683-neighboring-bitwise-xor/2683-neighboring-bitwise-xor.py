class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return self.helper(derived, 0) or self.helper(derived, 1)

    def helper(self, derived, firstBit):
        curBit = firstBit
        for b in derived:
            next = b^curBit
            curBit = next
        return next == firstBit