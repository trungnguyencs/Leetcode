class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        counter = Counter()
        ans = uniqCount = 0
        for i, ch in enumerate(s):
            if i >= k:
                prevChar = s[i-k]
                counter[prevChar] -= 1
                uniqCount -= 1 if counter[prevChar] == 0 else -1 if counter[prevChar] == 1 else 0
            counter[ch] += 1
            uniqCount += 1 if counter[ch] == 1 else -1 if counter[ch] == 2 else 0
            if uniqCount == k:
                ans += 1
        return ans