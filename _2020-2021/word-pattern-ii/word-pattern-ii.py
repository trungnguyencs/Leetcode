class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.chToWord, self.wordToCh = {}, {}
        return self.backtrack(pattern, s, 0, 0)
    
    def backtrack(self, pattern, s, i, j):
        if i == len(pattern) and j == len(s): return True
        if i == len(pattern) or j == len(s): return False
        ch = pattern[i]
        for k in range(j, len(s)):
            word = s[j:k+1]
            if ch in self.chToWord and self.chToWord[ch] != word: continue
            if word in self.wordToCh and self.wordToCh[word] != ch: continue
            if ch in self.chToWord:
                if self.backtrack(pattern, s, i+1, k+1): return True
                continue
            self.chToWord[ch], self.wordToCh[word] = word, ch
            if self.backtrack(pattern, s, i+1, k+1): return True
            del self.chToWord[ch]; del self.wordToCh[word]
        return False