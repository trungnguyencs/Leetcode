class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        counter = Counter()
        for ch in s:
            if ch in 'aeiouAEIOU':
                counter[ch] += 1
        vowels = sorted([[key, freq] for key, freq in counter.items()])
        j = 0
        for i, ch in enumerate(s):
            if ch in 'aeiouAEIOU':
                s[i] = vowels[j][0]
                vowels[j][1] -= 1
                if vowels[j][1] == 0:
                    j += 1
                    if j == len('aeiouAEIOU'):
                        break
        return ''.join(s)