class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.backtrack([], 1, n, k)
        return self.ans
        
    def backtrack(self, arr, i, n, k):
        if len(arr) == k:
            self.ans.append(arr[:])
            return
        for x in range(i, n + 1):
            if x not in arr:
                self.backtrack(arr + [x], x + 1, n, k)