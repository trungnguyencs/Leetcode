class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        #find the longest common subsequence (lcs) of s1 and s2
        #iterate s1 and s2, adding every char that is different to the current char in lcs
        lcs = self.longestCommonSubsequence(s1, s2)
        i = j = k = 0
        ans = []
        while i < len(s1) or j < len(s2):
            if i < len(s1) and j < len(s2) and k < len(lcs) and s1[i] == s2[j] == lcs[k]:
                ans.append(lcs[k])
                i, j, k = i + 1, j + 1, k + 1
            elif i < len(s1) and (k == len(lcs) or s1[i] != lcs[k]):
                ans.append(s1[i])
                i += 1
            elif j < len(s2) and (k == len(lcs) or s2[j] != lcs[k]):
                ans.append(s2[j])
                j += 1
        return ''.join(ans)

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        dp = [[''] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + s1[i-1]
                else:
                    dp[i][j] = max([dp[i-1][j], dp[i][j-1]], key=len)
        return dp[-1][-1]