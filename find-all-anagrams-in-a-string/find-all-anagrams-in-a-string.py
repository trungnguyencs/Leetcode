class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        counter = Counter(p)
        uniqCount = len(counter)
        w = len(p)
        for i, ch in enumerate(s):
            if i >= w:
                if s[i-w] in counter:
                    counter[s[i-w]] += 1
                    if counter[s[i-w]] == 1:
                        uniqCount += 1
            if ch in counter:
                counter[ch] -= 1
                if counter[ch] == 0:
                    uniqCount -= 1
                if uniqCount == 0:
                    ans.append(i - w + 1)
        return ans