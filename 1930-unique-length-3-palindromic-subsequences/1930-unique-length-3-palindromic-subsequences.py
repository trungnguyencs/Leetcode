class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for i in range(26):
            ch = chr(ord('a') + i)
            l, r = s.find(ch), s.rfind(ch)
            if l != r:
                ans += len(set(s[l+1:r]))
        return ans