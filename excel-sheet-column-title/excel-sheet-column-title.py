class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n > 0:
            n, charIdx = divmod(n-1, 26)
            ans.append(chr(ord('A') + charIdx))
        return ''.join(ans[::-1])
