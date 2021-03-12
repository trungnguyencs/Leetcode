class Solution:
    def numDecodings(self, s: str) -> int:
        # if s[0] == '0': return 0
        # dp = [0]*(len(s)+1)
        # dp[0], dp[1] = 1, 1
        # for i in range(1, len(s)):
        #     if s[i-1] not in '12': return 0
        #     dp_idx = i + 1
        #     if 10 <= int(s[i-1:i+1]) <= 26: dp[dp_idx] += dp[dp_idx-2]
        #     if 1 <= int(s[i]) <= 9: dp[dp_idx] += dp[dp_idx-1]
        # return dp[-1]
        
        # O(1) space
        if s[0] == '0': return 0
        prev, cur = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0' and s[i-1] not in '12': return 0
            nxt = 0
            if 1 <= int(s[i]) <= 9: nxt += cur
            if 10 <= int(s[i-1:i+1]) <= 26: nxt += prev
            prev, cur = cur, nxt
        return cur