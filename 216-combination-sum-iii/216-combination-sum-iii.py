class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.backtrack([], 1, k, n)
        return self.ans
    
    def backtrack(self, arr, i, k, n):
        if len(arr) == k and n == 0:
            self.ans.append(arr[:])
            return
        if len(arr) == k or n <= 0:
            return
        for num in range(i, 10):
            arr.append(num)
            self.backtrack(arr, num+1, k, n-num)
            arr.pop()