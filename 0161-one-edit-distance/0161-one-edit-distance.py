class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t): return self.canReplace(s, t)
        if len(s) + 1 == len(t): return self.canInsert(s, t)
        if len(t) + 1 == len(s): return self.canInsert(t, s)
        return False

    def canReplace(self, s, t):
        for i in range(len(s)):
            if s[i] != t[i]: return s[i+1:] == t[i+1:]
        return False
    
    def canInsert(self, s, t):
        for i in range(len(s)):
            if s[i] != t[i]: return s[i:] == t[i+1:]
        return True