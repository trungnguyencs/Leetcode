class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0]*(len(num1) + len(num2))
        for i, d1 in enumerate(reversed(num1)): # i, j start from 0
            for j, d2 in enumerate(reversed(num2)):
                ans[i+j] += int(d1) * int(d2)
                ans[i+j+1] += ans[i+j] // 10
                ans[i+j] %= 10
        while len(ans) > 1 and ans[-1] == 0: ans.pop()
        return ''.join(map(str, reversed(ans)))