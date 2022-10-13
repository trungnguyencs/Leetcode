class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.backtrack(s, [], 0)
        return self.ans
    
    def backtrack(self, s, arr, i):
        if i == len(s):
            self.ans.append(arr[:])
            return
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                self.backtrack(s, arr + [s[i:j+1]], j + 1)
    
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True