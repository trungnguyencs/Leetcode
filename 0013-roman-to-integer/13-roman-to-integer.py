class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for ch in reversed(s):
            val = dic[ch]
            ans += val if ans < 5 * val else -val
        return ans