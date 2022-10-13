class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.ans = set()
        self.backtrack([], n, k)
        return self.ans
    
    def backtrack(self, arr, n, k):
        if len(arr) == n:
            self.ans.add(int(''.join(list(map(str, arr)))))
            return
        if len(arr) == 0:
            for digit in range(1, 10):
                self.backtrack(arr + [digit], n, k)
        else:
            if arr[-1] - k >= 0:
                self.backtrack(arr + [arr[-1] - k], n, k)
            if arr[-1] + k <= 9:
                self.backtrack(arr + [arr[-1] + k], n, k)