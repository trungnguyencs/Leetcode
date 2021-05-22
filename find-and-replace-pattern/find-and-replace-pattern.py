class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = self.word2Num(pattern)
        ans = []
        for word in words:
            converted = self.word2Num(word)
            if converted == pattern: ans.append(word)
        return ans
        
    def word2Num(self, word):
        ch2Digit = {}
        digits = []
        for ch in word:
            if ch not in ch2Digit: ch2Digit[ch] = len(ch2Digit)
            digits.append(ch2Digit[ch])
        return digits