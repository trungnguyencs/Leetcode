class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                visited.add(i)
                self.dfs(i, isConnected, visited)
        return count
        
    def dfs(self, i, isConnected, visited):
        for j in range(len(isConnected)):
            if i != j and isConnected[i][j] and j not in visited:
                visited.add(j)
                self.dfs(j, isConnected, visited)