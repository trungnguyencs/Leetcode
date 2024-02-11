class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []
        for i, ch in enumerate(s):
            if i % 2 == 0:
                ans.append(ch)
            else:
                ans.append(chr(ord(s[i-1]) + int(ch)))
        return ''.join(ans)        