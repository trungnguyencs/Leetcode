class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = set(wordDict)
        self.ans = []
        self.backtrack(s, 0, [])
        return self.ans
        
    def backtrack(self, s, i, arr):
        if i == len(s):
            self.ans.append(' '.join(arr))
            return
        for j in range(i, len(s)):
            if s[i:j+1] in self.wordDict:
                self.backtrack(s, j+1, arr + [s[i:j+1]])