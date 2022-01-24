class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, longest = 0, 0
        uniq = defaultdict(int)
        for r, ch in enumerate(s):
            uniq[ch] += 1
            while len(uniq) > k:
                uniq[s[l]] -= 1
                if uniq[s[l]] == 0: del uniq[s[l]]
                l += 1
            longest = max(longest, r - l + 1)
        return longest