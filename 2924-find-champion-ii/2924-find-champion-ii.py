class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # topological sort works
        # better solution is finding the nodes where outdegree == 0
        outdegree = defaultdict(int)
        for s, e in edges:
            outdegree[e] += 1
        roots = [x for x in range(n) if outdegree[x] == 0]
        return roots[0] if len(roots) == 1 else -1    