class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        self.backtrack(s, wordDict, 0, [])
        return self.ans

    def backtrack(self, s, wordDict, i, arr):
        if i == len(s):
            self.ans.append(' '.join(arr))
            return
        for j in range(i, len(s)):
            word = s[i:j+1]
            if word in wordDict:
                self.backtrack(s, wordDict, j+1, arr+[word])