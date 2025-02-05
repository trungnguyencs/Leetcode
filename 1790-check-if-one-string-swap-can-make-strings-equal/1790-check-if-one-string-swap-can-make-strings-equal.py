class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        prev1 = prev2 = None
        diffSeen = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diffSeen += 1
                if diffSeen == 1:
                    prev1, prev2 = c1, c2
                elif diffSeen == 2:
                    if prev1 != c2 or prev2 != c1: return False
                else:
                    return False
        return diffSeen in (0, 2)