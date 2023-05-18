class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ind = defaultdict(int)
        for s, e in edges:
            ind[e] += 1
        return [x for x in range(n) if ind[x] == 0]