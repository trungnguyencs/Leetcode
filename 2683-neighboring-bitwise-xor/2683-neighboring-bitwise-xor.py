class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # original[i] ^ original[i + 1] = derived[i]
        # => original[i] ^ original[i] ^ original[i + 1] = original[i] ^ derived[i]
        # => original[i + 1] = original[i] ^ derived[i]
        # start with original[0] in [0, 1], and start xor with derived. Check if in the end it returns to the original value
        return self.helper(derived, 0) or self.helper(derived, 1)

    def helper(self, derived, firstBit):
        curBit = firstBit
        for b in derived:
            curBit ^= b
        return curBit == firstBit