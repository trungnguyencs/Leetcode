class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, maxLen = 0, 0
        for r, num in enumerate(A):
            if num == 0:
                K -= 1
            while K < 0:
                if A[l] == 0: K += 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen