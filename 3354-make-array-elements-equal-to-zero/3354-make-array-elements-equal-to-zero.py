class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        left = ans = 0
        #if at index i we have nums[i] == 0 and:
        #leftSum == rightSum -> ok to move left or move right
        #leftSum == rightSum + 1 -> ok to move left
        #rightSum == leftSum + 1 -> ok to move right
        for i in range(len(nums)):
            if nums[i] == 0:
                right = total - left
                if left == right:
                    ans += 2
                if abs(left - right) == 1:
                    ans += 1
            left += nums[i]
        return ans