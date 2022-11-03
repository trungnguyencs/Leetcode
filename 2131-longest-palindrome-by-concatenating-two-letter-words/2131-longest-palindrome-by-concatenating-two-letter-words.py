class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        maxPalindrome = 0
        hasOdd = False
        for word, count in counter.items():
            ch1, ch2 = word[0], word[1]
            if ch1 == ch2:
                if count % 2 == 1 and not hasOdd:
                    maxPalindrome += count*2
                    hasOdd = True
                else:
                    maxPalindrome += count//2*4
                counter[word] = 0
            elif ch2 + ch1 in counter:
                maxPalindrome += min(count, counter[ch2 + ch1])*4
                counter[word] = counter[ch2 + ch1] = 0
        return maxPalindrome