class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            if num > 0:
                stack.append(num)
                continue
            while stack and stack[-1] > 0 and stack[-1] < -num:
                stack.pop()
            if stack and stack[-1] == -num:
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(num)
        return stack