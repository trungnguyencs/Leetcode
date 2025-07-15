class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        hasVowel = hasConsonant = False
        for ch in word:
            if not (ch.isalpha() or ch.isdigit()):
                return False
            if ch in 'aeiouAEIOU':
                hasVowel = True
            elif not ch.isdigit():
                hasConsonant = True
        return hasVowel and hasConsonant