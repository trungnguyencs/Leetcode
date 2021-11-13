class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        ans = [0]*len(t)
        stack = []
        for i in range(len(t)-1, -1, -1):
            while stack and t[i] >= t[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans