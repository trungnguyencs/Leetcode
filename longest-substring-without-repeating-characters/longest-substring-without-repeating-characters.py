class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        l, longest = 0, 0
        for r, ch in enumerate(s):
            while ch in uniq:
                uniq.remove(s[l])
                l += 1
            uniq.add(ch)
            longest = max(longest, r - l + 1)
        return longest