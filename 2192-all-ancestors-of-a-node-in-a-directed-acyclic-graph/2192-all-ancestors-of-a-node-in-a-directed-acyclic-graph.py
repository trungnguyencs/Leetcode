class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        parentToChildren, ind = self.buildGraph(edges)
        q = deque(node for node in range(n) if ind[node] == 0)
        while q:
            node = q.popleft()
            for child in parentToChildren[node]:
                ans[child].add(node)
                ans[child].update(ans[node])
                ind[child] -= 1
                if ind[child] == 0:
                    q.append(child)
        return [sorted(s) for s in ans]
        
    def buildGraph(self, edges):
        parentToChildren = defaultdict(list)
        ind = defaultdict(int)
        for p, c in edges:
            parentToChildren[p].append(c)
            ind[c] += 1
        return parentToChildren, ind