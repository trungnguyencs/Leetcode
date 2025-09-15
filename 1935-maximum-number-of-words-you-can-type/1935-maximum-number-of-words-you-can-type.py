class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        ans = 0
        for word in text.split():
            if all(c not in brokenLetters for c in word):
                ans += 1
        return ans