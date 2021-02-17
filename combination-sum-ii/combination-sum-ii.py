class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.backtrack(candidates, 0, [], target)
        return self.ans
        
    def backtrack(self, candidates, i, arr, target):
        if target == 0:
            self.ans.append(arr[:])
            return
        if i == len(candidates) or target < 0: return
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]: continue
            arr.append(candidates[j])
            self.backtrack(candidates, j+1, arr, target - candidates[j])
            arr.pop()