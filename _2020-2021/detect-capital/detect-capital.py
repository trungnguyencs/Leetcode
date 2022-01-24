class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap = self.isCap(word[0])
        return all(self.isCap(ch) == cap for ch in word[1:]) or (cap and all(not self.isCap(ch) for ch in word[1:]))
            
    def isCap(self, ch):
        return ord('A') <= ord(ch) <= ord('Z')