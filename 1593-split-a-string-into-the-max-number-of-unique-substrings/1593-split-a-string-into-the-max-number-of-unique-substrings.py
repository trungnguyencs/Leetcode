class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        self.backtrack(s, 0, set())
        return self.ans
    
    def backtrack(self, s, i, visited):
        if i == len(s):
            self.ans = max(self.ans, len(visited))
            return
        for j in range(i, len(s)):
            if s[i:j+1] not in visited:
                visited.add(s[i:j+1])
                self.backtrack(s, j + 1, visited)
                visited.remove(s[i:j+1])