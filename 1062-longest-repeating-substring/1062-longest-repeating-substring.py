class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        visited = set()
        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                cur = s[i:j + 1]
                if cur in visited:
                    ans = max(ans, len(cur))
                elif len(cur) > ans:
                    visited.add(cur)
        return ans