class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dp = [0]*(len(words) + 1)
        for i in range(len(words)):
            dp[i+1] = dp[i] + 1 if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou' else dp[i]
        return [dp[e+1] - dp[s] for s, e in queries]