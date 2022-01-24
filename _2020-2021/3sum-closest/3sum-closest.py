class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.ans = self.closest = float('inf')
        for i in range(len(nums)-2):
            self.helper(nums, i, target)
            if self.closest == 0: break
        return self.ans
    
    def helper(self, nums, i, target):
        j, k = i+1, len(nums)-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            self.ans = min(self.ans, s, key=lambda x: abs(x-target))
            if s - target < 0:
                j += 1
            elif s - target > 0:
                k -= 1
            else: return
            