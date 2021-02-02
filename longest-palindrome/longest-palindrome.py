class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        hasOdd = False
        ans = 0
        for k, v in counter.items():
            if v % 2 == 1: 
                ans += v - 1
                hasOdd = True
            else:
                ans += v
        return ans + hasOdd