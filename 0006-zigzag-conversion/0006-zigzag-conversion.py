class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1: return s
        lst = ['' for _ in range(n)]
        for i, ch in enumerate(s):
            j = i % (2*n - 2)
            if j >= n:
                j = 2*n - 2 - j
            lst[j] += ch
        return ''.join(lst)