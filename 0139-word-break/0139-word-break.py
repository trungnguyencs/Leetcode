class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dp(i):
            if i == len(s): return True
            return any([dp(i + len(word)) for word in wordDict if i + len(word) <= len(s) and s[i:i+len(word)] == word])
        
        return dp(0)