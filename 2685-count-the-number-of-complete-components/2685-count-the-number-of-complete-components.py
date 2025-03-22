class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        G = self.buildGraph(edges)
        visited = set()
        ans = 0
        for i in range(n):
            if i not in visited and self.isCompleteComponent(i, G, visited):
                ans += 1
        return ans

    def isCompleteComponent(self, i, G, visited):
        nodeSet = set([i] + G[i])
        visited.update(nodeSet)
        for node in nodeSet:
            if len(G[node]) != len(nodeSet) - 1 or any(x not in nodeSet for x in G[node]):
                return False
        return True

    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G