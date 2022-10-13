class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.dic = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        self.ans = []
        self.backtrack(0, n, ['']*n)
        return self.ans
    
    def backtrack(self, i, n, arr):
        if i > n - i - 1:
            self.ans.append(''.join(arr))
            return
        if i == n - i - 1: # only when n is odd can this happen
            for d in "018":
                arr[i] = d
                self.backtrack(i + 1, n, arr)
        else:
            for key, val in self.dic.items():
                if i == 0 and key == '0': continue
                arr[i], arr[n-i-1] = key, val
                self.backtrack(i + 1, n, arr)