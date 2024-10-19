class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for _ in range(n):
            s += "1" + self.invert(s)[::-1]
        return s[k - 1]
    
    def invert(self, s):
        ans = []
        for ch in s:
            ans.append('0' if ch == '1' else '1')
        return ''.join(ans)