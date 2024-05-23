class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.backtrack(pattern, s, 0, 0, {}, {})
        
    def backtrack(self, pattern, s, i, j, dic1, dic2):
        if i == len(pattern) and j == len(s): return True
        if i == len(pattern) or j == len(s): return False
        ch = pattern[i]
        for k in range(j, len(s)):
            subS = s[j:k+1]
            if ch in dic1 and dic1[ch] != subS: continue
            if subS in dic2 and dic2[subS] != ch: continue
            if ch in dic1:
                if self.backtrack(pattern, s, i+1, k+1, dic1, dic2): return True
                continue
            dic1[ch], dic2[subS] = subS, ch
            if self.backtrack(pattern, s, i+1, k+1, dic1, dic2): return True
            del dic1[ch]; del dic2[subS]
        return False