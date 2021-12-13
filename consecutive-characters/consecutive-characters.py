class Solution:
    def maxPower(self, s: str) -> int:
        streak = maxStreak = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                streak += 1
                maxStreak = max(maxStreak, streak)
            else:
                streak = 1
        return maxStreak