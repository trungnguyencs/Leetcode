class Solution:
    def canFinish(self, numCourses: int, reqs: List[List[int]]) -> bool:
        G, indegree = self.buildGraph(reqs)
        q = deque([x for x in range(numCourses) if indegree[x] == 0])
        path = []
        while q:
            cur = q.popleft()
            path.append(cur)
            for parent in G[cur]:
                indegree[parent] -= 1
                if indegree[parent] == 0:
                    q.append(parent)
        return len(path) == numCourses
        
    def buildGraph(self, reqs):
        G = defaultdict(list)
        indegree = defaultdict(int)
        for s, e in reqs:
            indegree[s] += 1
            G[e].append(s)
        return G, indegree