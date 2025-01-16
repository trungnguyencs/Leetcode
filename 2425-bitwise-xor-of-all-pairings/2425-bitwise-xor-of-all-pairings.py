class Solution:
    def xorAllNums(self, A: List[int], B: List[int]) -> int:
        # We have (a^b)^(a^c)^(a^d)^... = (a^a^a^...)^(b^c^d^...)
        # => In the final xor each element of A will appears len(B) times, each element of B will appears len(A) times
        # Also if a number x is xored even times result will be 0, if odd times the result will be x
        ans = 0
        if len(B) % 2 == 1:
            for num in A:
                ans ^= num
        if len(A) % 2 == 1:
            for num in B:
                ans ^= num
        return ans