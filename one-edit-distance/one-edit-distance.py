class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t): return self.isOneEditDistance(t, s)
        if len(s) == len(t): return self.canReplace(s, t)
        if len(t) - len(s) == 1: return self.canInsert(s, t)
        return False
    
    def canReplace(self, s, t):
        for i in range(len(s)):
            if s[i] != t[i]: return s[i+1:] == t[i+1:]
        return False
        
    def canInsert(self, short, long):
        for i in range(len(short)):
            if short[i] != long[i]: return short[i:] == long[i+1:]
        return True