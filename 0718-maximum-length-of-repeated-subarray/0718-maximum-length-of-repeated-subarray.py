class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0]*(len(nums2) + 1)
        maxLen = 0
        for r in range(len(nums1)):
            tmp = [0]*(len(nums2) + 1)
            for c in range(len(nums2)):
                if nums1[r] == nums2[c]:
                    tmp[c+1] = 1 + dp[c]
                    maxLen = max(maxLen, tmp[c+1])
                else:
                    tmp[c+1] = 0
            dp = tmp
        return maxLen