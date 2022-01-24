class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()
        G = self.buildGraph(isConnected)
        for node in range(len(isConnected)):
            if node not in visited:
                count += 1
                self.dfs(node, G, visited)
        return count
        
    def dfs(self, node, G, visited):
        visited.add(node)
        for neigh in G[node]:
            if neigh not in visited:
                self.dfs(neigh, G, visited)
                
    def buildGraph(self, isConnected):
        G = defaultdict(list)
        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if r != c and isConnected[r][c]:
                    G[r].append(c)
        return G