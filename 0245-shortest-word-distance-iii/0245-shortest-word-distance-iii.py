class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        minDistance = len(words)
        i1 = i2 = float('-inf')
        sameWord = word1 == word2
        for i, word in enumerate(words):
            if word == word1:
                minDistance = min(minDistance, i - i2)
                i1 = i
            if word == word2:
                if not sameWord:
                    minDistance = min(minDistance, i - i1)
                i2 = i
        return minDistance