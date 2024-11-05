class Solution:
    def minChanges(self, s: str) -> int:
        flips = 0
        streak = 1
        cur = s[0]
        for i in range(1, len(s)):
            if s[i] == cur:
                streak += 1
            elif streak % 2 == 1:
                flips += 1
                streak += 1
            else:
                cur = s[i]
                streak = 1
        return flips