class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for ch, freq in counter.items():
            ans += freq if (freq % 2 == 0 or ans % 2 == 0) else freq - 1
        return ans