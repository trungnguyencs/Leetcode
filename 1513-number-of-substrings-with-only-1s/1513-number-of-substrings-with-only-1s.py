class Solution:
    def numSub(self, s: str) -> int:
        ans = streak = 0
        for ch in s:
            if ch == '1':
                streak += 1
                ans += streak
            else:
                streak = 0
        return ans % (10**9 + 7)