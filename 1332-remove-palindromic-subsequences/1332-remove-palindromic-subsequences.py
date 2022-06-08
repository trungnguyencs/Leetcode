class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if self.isPalindrome(s) else 2
    
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True