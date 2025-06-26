class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        #We greedly take all 0s, and try to take as many 1s as possible.
        #To take the 1 with smaller cost, we take the 1s from rightmost.
        #Time O(n), Space O(1)
        ans = cur = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                ans += 1
            elif cur + 2**(len(s) - 1 - i) <= k:
                cur += 2**(len(s) - 1 - i)
                ans += 1
        return ans