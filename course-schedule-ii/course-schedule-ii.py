class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree, G = self.buildGraph(prerequisites)
        path = []
        q = deque([node for node in range(numCourses) if indegree[node] == 0])
        while q:
            cur = q.popleft()
            path.append(cur)
            for s in G[cur]:
                indegree[s] -= 1
                if indegree[s] == 0:
                    q.append(s)
        return path if len(path) == numCourses else []    
        
    def buildGraph(self, prerequisites):
        indegree = defaultdict(int)
        G = defaultdict(set)
        for s, e in prerequisites:
            indegree[s] += 1
            G[e].add(s)
        return indegree, G
​
