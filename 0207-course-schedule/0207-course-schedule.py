class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G, ind = self.buildGraph(prerequisites)
        q = deque()
        for c in range(numCourses):
            if ind[c] == 0:
                q.append(c)
        finished = 0
        while q:
            cur = q.popleft()
            finished += 1
            for p in G[cur]:
                ind[p] -= 1
                if ind[p] == 0:
                    q.append(p)
        return finished == numCourses

    def buildGraph(self, prerequisites):
        ind = defaultdict(int)
        G = defaultdict(set)
        for p, c in prerequisites:
            G[c].add(p)
            ind[p] += 1
        return G, ind
