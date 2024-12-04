class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        i = 0
        for ch in s1:
            if s2[i] in (ch, self.getWrapAroundChar(ch)):
                i += 1
                if i == len(s2): return True
        return False
            
    def getWrapAroundChar(self, ch):
        d = (ord(ch) - ord('a') + 1) % 26
        newCh = chr(ord('a') + d)
        return newCh