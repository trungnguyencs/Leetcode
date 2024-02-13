class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.isPalindrome(w): return w
        return ''
        
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True