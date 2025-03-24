class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dp will take O(n^2)
        #greedy O(n): going from the back of the array, at each index find out if it can be reached
        cur = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= cur:
                cur = i
        return cur == 0