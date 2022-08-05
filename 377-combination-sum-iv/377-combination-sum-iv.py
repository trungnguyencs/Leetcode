class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.nums = nums
        return self.dp(target)
        
    @cache
    def dp(self, target):
        if target < 0: return 0
        if target == 0: return 1
        return sum(self.dp(target - x) for x in self.nums)