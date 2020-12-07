class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        ans = -1
        for i, ch in enumerate(s):
            if ch in dic:
                ans = max(ans, i - dic[ch] - 1)
            else:
                dic[ch] = i
        return ans
