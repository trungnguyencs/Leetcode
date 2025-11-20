class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums) - 2):
            ans += self.helper(nums, i, target)
        return ans

    def helper(self, nums, i, target):
        ans = 0
        j, k = i + 1, len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < target: #fix j: all triplets (i, j, j+1...k) would satisfy
                ans += k - j
                j += 1
            else:
                k -= 1
        return ans