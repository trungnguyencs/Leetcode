class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            tmp = []
            cur, count = s[0], 1
            for i in range(1, len(s)):
                if s[i] == cur:
                    count += 1
                else:
                    tmp.extend([str(count), cur])
                    cur, count = s[i], 1
            tmp.extend([str(count), cur])
            s = ''.join(tmp)
        return s              