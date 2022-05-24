class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp, stack = [0]*(len(s) + 1), [] # dp[i] = length of valid paren ending at i-1
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if stack:
                    open = stack.pop()
                    dp[i+1] = dp[open] + i - open + 1
        return max(dp)