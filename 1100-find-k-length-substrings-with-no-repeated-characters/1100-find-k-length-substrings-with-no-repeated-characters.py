class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        counter = Counter()
        ans = 0
        for i, ch in enumerate(s):
            counter[ch] += 1
            if i >= k:
                prevChar = s[i-k]
                counter[prevChar] -= 1
                if counter[prevChar] == 0:
                    del counter[prevChar]
            if len(counter) == k:
                ans += 1
        return ans