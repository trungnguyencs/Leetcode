class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for num, freq in counter.items():
            if freq % 2 == 0 or ans % 2 == 0:
                ans += freq
            else:
                ans += freq - 1
        return ans