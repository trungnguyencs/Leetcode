class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = Counter()
        l, maxLen = 0, 0
        for r, ch in enumerate(s):
            counter[ch] += 1
            while len(counter) == 3:
                counter[s[l]] -= 1
                if counter[s[l]] == 0: del counter[s[l]]
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen