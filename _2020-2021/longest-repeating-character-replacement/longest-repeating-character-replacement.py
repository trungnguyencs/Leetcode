class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        l = maxFrequency = maxLen = 0
        for r, ch in enumerate(s):
            counter[ch] += 1
            maxFrequency = max(maxFrequency, counter[ch])
            if r - l + 1 > maxFrequency + k:
                counter[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen