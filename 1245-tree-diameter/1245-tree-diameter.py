class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.G = defaultdict(list)
        for s, e in edges:
            self.G[s].append(e)
            self.G[e].append(s)
        self.visited = {0}
        self.longestPath = 1
        self.postOrder(0)
        return self.longestPath - 1
    
    def postOrder(self, root):
        childPaths = []
        for neigh in self.G[root]:
            if neigh in self.visited:
                continue
            self.visited.add(neigh)
            childPaths.append(self.postOrder(neigh))
        childPaths.sort(reverse=True)
        if len(childPaths) == 0: return 1
        if len(childPaths) == 1:
            self.longestPath = max(self.longestPath, 1 + childPaths[0])
        else:
            self.longestPath = max(self.longestPath, 1 + childPaths[0] + childPaths[1])
        return 1 + childPaths[0]