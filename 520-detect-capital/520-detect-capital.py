class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitalCount = 0
        for ch in word:
            if ch.isupper():
                capitalCount += 1
        return capitalCount in [0, len(word)] or capitalCount == 1 and word[0].isupper()