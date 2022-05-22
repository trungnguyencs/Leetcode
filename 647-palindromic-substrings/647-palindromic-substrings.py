class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(self.expand(s, i, i) + self.expand(s, i, i+1) for i in range(len(s)))
        
    def expand(self, s, l, r):
        ans = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        return ans