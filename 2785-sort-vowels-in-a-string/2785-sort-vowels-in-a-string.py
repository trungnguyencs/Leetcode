class Solution:
    def sortVowels(self, s: str) -> str:
        ans = ['']*len(s)
        counter = Counter()
        for i, ch in enumerate(s):
            if ch not in 'aeiouAEIOU':
                ans[i] = ch
            else:
                counter[ch] += 1
        vowels = sorted([ch, count] for ch, count in counter.items())
        print(vowels)
        i = 0
        for j, ch in enumerate(ans):
            if ch == '':
                while vowels[i][1] == 0:
                    i += 1
                ans[j] = vowels[i][0]
                vowels[i][1] -= 1
        return ''.join(ans)