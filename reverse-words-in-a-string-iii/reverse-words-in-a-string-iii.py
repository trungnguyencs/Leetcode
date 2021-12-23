class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l = 0
        for r, ch in enumerate(s):
            if r == len(s) - 1:
                self.reverse(s, l, r)
            elif ch == ' ':
                self.reverse(s, l, r - 1)
                l = r + 1
        return ''.join(s)
        
    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1