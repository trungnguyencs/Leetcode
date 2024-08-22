class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.ans = []
        self.backtrack(word, 0, [])
        return self.ans
        
    def backtrack(self, word, i, arr):
        if i == len(word):
            self.ans.append(''.join([str(e) for e in arr]))
            return
        self.backtrack(word, i + 1, arr + [word[i]])
        if arr and type(arr[-1]) == type(0): return
        for j in range(i, len(word)):
            self.backtrack(word, j + 1, arr + [j - i + 1])