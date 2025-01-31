class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree if both:
        # 1. there's only 1 connected component
        # 2. #edges = #nodes - 1
        if len(edges) != n - 1: return False
        G = self.buildGraph(edges)
        visited = {0}
        return self.dfs(0, G, visited) == n

    def dfs(self, node, G, visited):
        nodeCount = 1
        for neigh in G[node]:
            if neigh not in visited:
                visited.add(neigh)
                nodeCount += self.dfs(neigh, G, visited)
        return nodeCount

    def buildGraph(self, edges):
        G = defaultdict(set)
        for s, e in edges:
            G[s].add(e)
            G[e].add(s)
        return G