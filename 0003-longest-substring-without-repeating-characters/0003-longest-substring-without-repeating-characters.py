class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = maxLen = 0
        uniq = set()
        for r, ch in enumerate(s):
            while ch in uniq:
                uniq.remove(s[l])
                l += 1
            uniq.add(ch)
            maxLen = max(maxLen, r - l + 1)
        return maxLen