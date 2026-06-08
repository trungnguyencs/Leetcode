class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        middle = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num < middle:
                return True
            while stack and stack[-1] < num:
                middle = stack.pop()
            stack.append(num)
        return False