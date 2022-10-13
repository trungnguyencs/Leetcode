class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(0, target, candidates, [])
        return self.ans
    
    def backtrack(self, i, target, candidates, arr):
        if target == 0:
            self.ans.append(arr[:])
            return
        if target < 0:
            return
        for j in range(i, len(candidates)):
            arr.append(candidates[j])
            self.backtrack(j, target - candidates[j], candidates, arr)
            arr.pop()