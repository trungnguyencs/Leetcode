class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDistance = float('inf')
        i1 = i2 = float('-inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                minDistance = min(minDistance, i - i2)
                i1 = i
            elif word == word2:
                minDistance = min(minDistance, i - i1)
                i2 = i
        return minDistance