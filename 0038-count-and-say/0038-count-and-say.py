class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        s = self.countAndSay(n - 1) + '#'
        cur, count = s[0], 0
        ans = []
        for ch in s:
            if ch == cur:
                count += 1
            else:
                ans.extend([str(count), cur])
                cur, count = ch, 1
        return ''.join(ans)