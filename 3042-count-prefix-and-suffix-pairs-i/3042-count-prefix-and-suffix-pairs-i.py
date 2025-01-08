class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, word in enumerate(words):
            n = len(word)
            for j in range(i + 1, len(words)):
                word2 = words[j]
                if i != j and len(word) <= len(word2) and word2[:n] == word2[-n:] == word:
                    ans += 1
        return ans