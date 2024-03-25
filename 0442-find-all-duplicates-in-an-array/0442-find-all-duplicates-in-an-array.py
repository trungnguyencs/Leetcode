class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            num = abs(num)
            idx = num - 1
            if nums[idx] < 0:
                ans.append(num)
            else:
                nums[idx] *= -1
        return ans