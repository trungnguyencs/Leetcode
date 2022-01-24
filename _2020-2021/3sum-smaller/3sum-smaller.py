class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.ans = 0
        for i in range(len(nums)-2):
            self.helper(nums, i, target - nums[i])
        return self.ans
    
    def helper(self, nums, i, target):
        l, r = i+1, len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                self.ans += r - l # fix l, any r in [l+1, r] will satisfy
                l += 1
            else:
                r -= 1