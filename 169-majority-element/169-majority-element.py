class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, vote = nums[0], 1
        for num in nums[1:]:
            vote += 1 if num == ans else -1
            if vote == 0:
                ans, vote = num, 1
        return ans