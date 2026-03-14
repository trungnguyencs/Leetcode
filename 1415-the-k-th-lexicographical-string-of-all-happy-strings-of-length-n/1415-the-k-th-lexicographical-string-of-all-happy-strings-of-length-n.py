class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.k = k
        return self.backtrack([''] * n, 0)

    def backtrack(self, arr, i):
        if i == len(arr):
            self.k -= 1
            if self.k == 0:
                return ''.join(arr)
            return ''
        for ch in 'abc':
            if i > 0 and ch == arr[i-1]:
                continue
            arr[i] = ch
            res = self.backtrack(arr, i + 1)
            if res: return res
        return ''