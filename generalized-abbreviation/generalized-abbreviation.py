class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.ans = []
        self.backtrack(word, [], 0)
        return self.ans
    
    def backtrack(self, word, arr, i):
        if i == len(word):
            self.ans.append(''.join(list(map(lambda x: str(x), arr))))
            return
        if i > 0 and type(arr[-1]) == type(0):
            arr[-1] += 1
            self.backtrack(word, arr, i + 1)
            arr[-1] -= 1
        else:
            self.backtrack(word, arr + [1], i + 1)
        self.backtrack(word, arr + [word[i]], i + 1)