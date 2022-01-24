class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if ans: return ans
                continue
            ans += 1
        return ans
