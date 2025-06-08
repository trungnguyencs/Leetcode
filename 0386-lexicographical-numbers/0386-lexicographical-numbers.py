class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.ans = []
        self.n = n
        for i in range(1, 10):
            self.dfs(i)
        return self.ans

    def dfs(self, x):
        if x > self.n:
            return
        self.ans.append(x)
        for i in range(10):
            self.dfs(x * 10 + i)