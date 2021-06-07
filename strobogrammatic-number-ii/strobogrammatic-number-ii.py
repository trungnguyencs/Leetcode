class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.dic = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        self.ans = []
        self.backtrack(['']*n, 0, n)
        return self.ans

    def backtrack(self, s, i, n):
        if i == n//2:
            if n % 2 == 1:
                for ch in '018':
                    s[i] = ch
                    self.ans.append(''.join(s))
            else:
                self.ans.append(''.join(s))
            return
        for ch in self.dic:
            if n > 1 and (i, ch) == (0, '0'): continue
            s[i], s[n-1-i] = ch, self.dic[ch]
            self.backtrack(s, i+1, n)