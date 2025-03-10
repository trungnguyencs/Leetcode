class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        #similar questions: 992. Subarrays with K Different Integers
        #which is a harder version of 340. Longest Substring with At Most K Distinct Characters
        return self.atLeastK(word, k) - self.atLeastK(word, k + 1)

    def atLeastK(self, word, k):
        l = ans = 0
        vowels = Counter()
        consonants = 0
        for r, ch in enumerate(word):
            if ch in 'aeiou':
                vowels[ch] += 1
            else:
                consonants += 1
            while len(vowels) == 5 and consonants >= k:
                ans += len(word) - r #all strings with ending index >= r will qualify
                prev = word[l]
                if prev in 'aeiou':
                    vowels[prev] -= 1
                    if vowels[prev] == 0:
                        del vowels[prev]
                else:
                    consonants -= 1
                l += 1
        return ans