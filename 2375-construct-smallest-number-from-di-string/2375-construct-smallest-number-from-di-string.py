class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.ans = []
        self.backtrack([0] * (len(pattern) + 1), 0, pattern)
        return ''.join([str(d) for d in self.ans])

    def backtrack(self, arr, i, pattern):
        if i == len(pattern) + 1:
            self.ans = arr[:]
            return True
        for d in range(1, 10): #go from smallest, the first that satisfies is the answer
            if d in arr: continue
            if i == 0 or (pattern[i-1] == 'D' and d < arr[i-1]) or (pattern[i-1] == 'I' and d > arr[i-1]):
                arr[i] = d
                if self.backtrack(arr, i + 1, pattern): return True
        return False