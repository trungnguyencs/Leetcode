class Solution:
    def minimumSemesters(self, n: int, edges: List[List[int]]) -> int:
        G, ind = self.buildGraph(edges)
        q = deque([i for i in range(1, n + 1) if ind[i] == 0])
        step = visitedCount = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                visitedCount += 1
                for parent in G[cur]:
                    ind[parent] -= 1
                    if ind[parent] == 0:
                        q.append(parent)
            step += 1
        return step if visitedCount == n else -1
        
    def buildGraph(self, edges):
        G = defaultdict(set)
        ind = defaultdict(int)
        for s, e in edges:
            G[e].add(s)
            ind[s] += 1
        return G, ind