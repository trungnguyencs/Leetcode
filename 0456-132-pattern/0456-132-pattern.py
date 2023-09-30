class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Find array of '1'
        m = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            m[i] = min(m[i-1], nums[i])
        # Stack stores '2'
        stack = []
        # Iterate with '3'
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= m[i]:
                stack.pop()
            if stack and m[i] < stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
        return False