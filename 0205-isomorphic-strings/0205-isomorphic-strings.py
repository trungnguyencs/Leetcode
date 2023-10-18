class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dic1, dic2 = {}, {}
        for c1, c2 in zip(s, t):
            if c1 in dic1 and dic1[c1] != c2: return False
            dic1[c1] = c2
            if c2 in dic2 and dic2[c2] != c1: return False
            dic2[c2] = c1
        return True