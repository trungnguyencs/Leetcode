class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        ans = set()
        for i in range(len(s)):
            counter = Counter()
            for j in range(i, len(s)):
                ch = s[j]
                counter[ch] += 1
                if len(set(counter.values())) == 1:
                    ans.add(s[i:j+1])
        return len(ans)