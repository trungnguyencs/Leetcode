class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        chToWord, wordToCh = {}, {}
        for ch, word in zip(pattern, s):
            if ch in chToWord and chToWord[ch] != word: return False
            if word in wordToCh and wordToCh[word] != ch: return False
            chToWord[ch] = word
            wordToCh[word] = ch
        return True