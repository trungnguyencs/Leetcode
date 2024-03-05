class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: break
            cur = s[l]
            while l <= r and s[l] == cur:
                l += 1
            while l <= r and s[r] == cur:
                r -= 1
        return r - l + 1