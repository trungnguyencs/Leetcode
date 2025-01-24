class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #use Topological sort
        ind, parents = self.buildGraph(graph)
        q = deque([node for node in range(len(graph)) if ind[node] == 0])
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            for parent in parents[cur]:
                ind[parent] -= 1
                if ind[parent] == 0:
                    q.append(parent)
        return sorted(ans)

    def buildGraph(self, graph):
        ind = defaultdict(int)
        parents = defaultdict(set)
        for parent, childrens in enumerate(graph):
            for child in childrens:
                parents[child].add(parent)
                ind[parent] += 1
        return ind, parents