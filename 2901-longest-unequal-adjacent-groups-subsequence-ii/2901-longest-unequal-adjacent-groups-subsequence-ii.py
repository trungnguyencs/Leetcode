class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [[w] for w in words]
        for i in range(1, len(dp)):
            for j in range(i):
                if self.hasHammingDistanceOne(words[i], words[j]) and groups[i] != groups[j]:
                    dp[i] = max(dp[i], dp[j] + [words[i]], key=len)
        return max(dp, key=len)

    def hasHammingDistanceOne(self, word1, word2):
        if len(word1) != len(word2): return False
        return sum([c1 != c2 for c1, c2 in zip(word1, word2)]) == 1