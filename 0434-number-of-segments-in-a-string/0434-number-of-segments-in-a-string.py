class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s):
            if ch != ' ' and (i == 0 or s[i-1] == ' '):
                ans += 1
        return ans