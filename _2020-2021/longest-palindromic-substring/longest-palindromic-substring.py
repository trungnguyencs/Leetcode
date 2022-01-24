class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            longest = max(longest, self.expand(s, i, i), self.expand(s, i, i+1), key=len)
        return longest
    
    def expand(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]: break
            i -= 1
            j += 1
        return s[i+1:j]