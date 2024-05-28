class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = r = maxLen = cost = 0
        for r in range(len(s)):
            cost += abs(ord(s[r]) - ord(t[r]))
            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen