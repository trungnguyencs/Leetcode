class Solution:
    def buddyStrings(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        seenDiff = False
        for i, (c1, c2) in enumerate(zip(s, t)):
            if c1 != c2:
                if not seenDiff:
                    seenDiff = True
                    s1, t1 = c1, c2
                else:
                    return s1 == c2 and t1 == c1 and s[i+1:] == t[i+1:]
        return (not seenDiff) and len(s) > len(set(s))