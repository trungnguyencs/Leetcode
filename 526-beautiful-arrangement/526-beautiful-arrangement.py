class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        self.backtrack(0, n, [0]*n, set())
        return self.ans
    
    def backtrack(self, i, n, arr, visited):
        if i == n:
            self.ans += 1
            return
        for num in range(1, n + 1):
            if num in visited: continue
            if 0 in [num % (i + 1), (i + 1) % num]:
                arr[i] = num
                visited.add(num)
                self.backtrack(i + 1, n, arr, visited)
                visited.remove(num)