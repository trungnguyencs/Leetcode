class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1 = j1 = i2 = j2 = 0 
        while i1 < len(word1) and i2 < len(word2):
            while i1 < len(word1) and j1 == len(word1[i1]):
                i1, j1 = i1 + 1, 0
            while i2 < len(word2) and j2 == len(word2[i2]):
                i2, j2 = i2 + 1, 0
            if i1 < len(word1) and i2 < len(word2):
                if word1[i1][j1] != word2[i2][j2]: return False
                j1 += 1
                j2 += 1
        return (i1, i2, j1, j2) == (len(word1), len(word2), 0, 0)