class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        diff = 0
        prev1 = prev2 = ''
        for c1, c2 in zip(s1, s2):
            if c1 == c2: continue
            diff += 1
            if diff == 1: prev1, prev2 = c1, c2
            if diff == 2 and (c1, c2) != (prev2, prev1): return False
            if diff == 3: return False
        return diff != 1