class Solution:
    def check(self, nums: List[int]) -> bool:
        dips = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                dips += 1
                if dips == 2: return False
        if dips == 0: return True
        return nums[-1] <= nums[0]