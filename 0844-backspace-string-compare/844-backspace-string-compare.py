class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            ch1, ch2 = '', ''
            i, ch1 = self.helper(s, i)
            j, ch2 = self.helper(t, j)
            if ch1 != ch2: return False
        return True
                
    def helper(self, s, i):
        count = 0
        ch = ''
        while i >= 0 and ch == '':
            if s[i] == '#':
                count += 1
            elif count > 0:
                count -= 1
            else:
                ch = s[i]
            i -= 1
        return i, ch