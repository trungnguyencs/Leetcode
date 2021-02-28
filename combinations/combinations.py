class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(n, k, 1, [])
        return self.ans
    
    def backtrack(self, n, k, i, arr):
        if len(arr) == k:
            self.ans.append(arr[:])
        for j in range(i, n+1):
            arr.append(j)
            self.backtrack(n, k, j+1, arr)
            arr.pop()