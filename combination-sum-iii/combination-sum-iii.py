class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.backtrack([], 1, k, n)
        return self.ans
        
    def backtrack(self, arr, i, k, n):
        if len(arr) == k and n == 0:
            self.ans.append(arr[:])
            return
        elif len(arr) == k or n < 0: return
        for j in range(i, 10):
            self.backtrack(arr+[j], j+1, k, n-j)