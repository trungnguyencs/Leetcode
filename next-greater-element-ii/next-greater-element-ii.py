class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        circularNums = nums + nums
        ans = [-1]*len(nums)
        stack = []
        for i, num in enumerate(circularNums):
            while stack and num > stack[-1][1]:
                j, _ = stack.pop()
                ans[j] = num
            if i < len(nums):
                stack.append((i, num))
        return ans