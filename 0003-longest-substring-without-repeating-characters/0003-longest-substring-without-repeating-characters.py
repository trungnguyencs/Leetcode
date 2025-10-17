class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l = ans = 0
        for r, ch in enumerate(s):
            while ch in unique:
                unique.remove(s[l])
                l += 1
            unique.add(ch)
            ans = max(ans, r - l + 1)
        return ans