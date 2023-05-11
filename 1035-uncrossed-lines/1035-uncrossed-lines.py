class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # same as 1143. Longest Common Subsequence
        dp = [[0]*(len(nums1) + 1) for _ in range(len(nums2) + 1)]
        for r in range(1, len(nums2) + 1):
            for c in range(1, len(nums1) + 1):
                if nums1[c - 1] == nums2[r - 1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]