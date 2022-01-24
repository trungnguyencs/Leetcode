class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        self.backtrack([], set(), n)
        return self.ans
    
    def backtrack(self, arr, visited, n):
        if len(arr) == n:
            self.ans += 1
            return
        i = len(arr) + 1
        for num in range(1, n + 1):
            if num in visited or not (num % i == 0 or i % num == 0):
                continue
            arr.append(num)
            visited.add(num)
            self.backtrack(arr, visited, n)
            arr.pop()
            visited.remove(num)