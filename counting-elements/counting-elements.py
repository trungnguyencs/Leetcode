class Solution:
    def countElements(self, nums: List[int]) -> int:
        uniq = set(nums)
        count = 0
        for num in nums:
            if num + 1 in uniq:
                count += 1
        return count