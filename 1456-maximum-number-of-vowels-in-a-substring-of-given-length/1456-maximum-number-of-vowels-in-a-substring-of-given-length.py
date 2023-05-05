class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = maxVowels = 0
        for i, ch in enumerate(s):
            if i >= k:
                if s[i-k] in 'aeiou':
                    vowels -= 1
            if ch in 'aeiou':
                vowels += 1
            maxVowels = max(maxVowels, vowels)
        return maxVowels