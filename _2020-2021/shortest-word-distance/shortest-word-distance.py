class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1, i2 = float('-inf'), float('-inf')
        minDistance = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                minDistance = min(minDistance, i - i2) 
                i1 = i
            elif words[i] == word2:
                minDistance = min(minDistance, i - i1)
                i2 = i
        return minDistance