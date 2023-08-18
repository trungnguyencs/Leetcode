class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        edges = set()            
        degree = defaultdict(int)
        for s, e in roads:
            degree[s] += 1
            degree[e] += 1
            edges.add((s, e))
            edges.add((e, s))
        sameDegree = defaultdict(list)
        for node, degree in degree.items():
            sameDegree[degree].append(node)
        Max = max(sameDegree.keys())
        secondMax = 0
        for k in sameDegree.keys():
            if k > secondMax and k != Max:
                secondMax = k
        maxNodes = sameDegree[Max]
        secondMaxNodes = sameDegree[secondMax]
        if len(maxNodes) >= 2:
            return 2*Max if any((i, j) not in edges for i in maxNodes for j in maxNodes if i != j) else 2*Max - 1
        else:
            return Max + secondMax if any((i, j) not in edges for i in maxNodes for j in secondMaxNodes) else Max + secondMax - 1