class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum(f * (f + 1) // 2 for f in Counter(s).values())