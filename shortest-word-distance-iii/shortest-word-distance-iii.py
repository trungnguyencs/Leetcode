class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lastIdx1 = lastIdx2 = float('-inf')
        minDistance = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1 == word2:
                minDistance = min(minDistance, i - lastIdx1)
                lastIdx1 = i
            elif word == word1:
                minDistance = min(minDistance, i - lastIdx2)
                lastIdx1 = i
            elif word == word2:
                minDistance = min(minDistance, i - lastIdx1)
                lastIdx2 = i
        return minDistance                