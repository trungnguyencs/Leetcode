class Solution:
    def maxLength(self, arr: List[str]) -> int:
        candidates = [w for w in arr if len(w) == len(set(w))]
        self.longest = 0
        self.backtrack(candidates, 0, '')
        return self.longest
    
    def backtrack(self, candidates, i, cur):
        if i == len(candidates):
            self.longest = max(self.longest, len(cur))
            return
        for j in range(i, len(candidates)):  
            if any(ch in cur for ch in candidates[j]):
                self.backtrack(candidates, j + 1, cur)
            else:
                self.backtrack(candidates, j + 1, cur + candidates[j])