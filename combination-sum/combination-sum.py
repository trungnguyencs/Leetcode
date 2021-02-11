class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(candidates, 0, [], target)
        return self.ans
        
    def backtrack(self, candidates, i, arr, target):
        if target == 0:
            self.ans.append(arr[:])
            return
        if target < 0:
            return
        for j in range(i, len(candidates)):
            arr.append(candidates[j])
            self.backtrack(candidates, j, arr, target-candidates[j])
            arr.pop()