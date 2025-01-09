class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False]*(len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict and dp[i]:
                    dp[j+1] = True
        return dp[-1]