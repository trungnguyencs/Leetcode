class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        G, ind = self.buildGraph(prerequisites, n)
        q = deque([i for i in range(n) if ind[i] == 0])
        courseOrder = []
        while q:
            child = q.popleft()
            courseOrder.append(child)
            for parent in G[child]:
                ind[parent] -= 1
                if ind[parent] == 0:
                    q.append(parent)
        return len(courseOrder) == n
            
    def buildGraph(self, prerequisites, n):
        G = defaultdict(list)
        ind = [0]*n
        for parent, child in prerequisites:
            ind[parent] += 1
            G[child].append(parent)
        return G, ind