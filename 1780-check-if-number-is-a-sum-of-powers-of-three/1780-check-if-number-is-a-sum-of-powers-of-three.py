class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        #there's a math solution but conditions allow backtracking
        if n == 0: return False
        return self.dfs(n, 1)

    def dfs(self, n, p):
        if n == 0: return True
        if n < p: return False
        return self.dfs(n, p * 3) or self.dfs(n - p, p * 3)