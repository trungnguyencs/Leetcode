class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark a visited number by turning negative the number
        # whose index equals to (the visited number-1)
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] *= -1
        return [i for i in range(1, len(nums)+1) if nums[i-1] > 0]
            