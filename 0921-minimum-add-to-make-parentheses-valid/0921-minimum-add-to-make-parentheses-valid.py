class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        ans = 0
        for ch in s:
            if ch == '(':
                open += 1
            elif open > 0:
                open -= 1
            else:
                ans += 1
        return ans + open