class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        l = longest = 0
        for r, ch in enumerate(s):
            dic[ch] += 1
            while len(dic) > k:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            longest = max(longest, r - l + 1)
        return longest