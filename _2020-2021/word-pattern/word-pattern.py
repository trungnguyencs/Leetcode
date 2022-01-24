class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s): return False
        return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))