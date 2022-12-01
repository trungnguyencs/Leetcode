class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return self.countVowels(s, 0, len(s)//2 - 1) == self.countVowels(s, len(s)//2, len(s) - 1)
        
    def countVowels(self, s, i, j):
        return sum(s[i] in 'aeiouAEIOU' for i in range(i, j + 1))