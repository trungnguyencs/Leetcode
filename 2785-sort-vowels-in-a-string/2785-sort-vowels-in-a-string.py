class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        counter = Counter()
        pos = []
        for i, ch in enumerate(s):
            if ch in 'aeiouAEIOU':
                counter[ch] += 1
                pos.append(i)
        vowels = sorted([[key, freq] for key, freq in counter.items()])
        j = 0
        for i in pos:
            s[i] = vowels[j][0]
            vowels[j][1] -= 1
            if vowels[j][1] == 0:
                j += 1
                if j == len('aeiouAEIOU'):
                    break
        return ''.join(s)