class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0: continue
            nums[num - 1] *= -1
        return [i + 1 for i, num in enumerate(nums) if num > 0]