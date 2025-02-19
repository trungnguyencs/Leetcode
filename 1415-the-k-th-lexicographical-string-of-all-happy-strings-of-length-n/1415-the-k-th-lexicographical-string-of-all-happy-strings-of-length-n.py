class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.k = k
        self.ans = ''
        self.backtrack([], n)
        return self.ans

    def backtrack(self, arr, n):
        if len(arr) == n:
            self.k -= 1
            if self.k == 0:
                self.ans = ''.join(arr)
            return
        for ch in 'abc':
            if len(arr) > 0 and arr[-1] == ch:
                continue
            if self.k > 0:
                self.backtrack(arr + [ch], n)