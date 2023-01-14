class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parents = list(range(26))
        
        def find(x):
            while x != parents[x]:
                x = parents[x]
            return x
                
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX < rootY:
                parents[rootY] = rootX
            else:
                parents[rootX] = rootY
                
        def chToIdx(c):
            return ord(c) - ord('a')
        
        def idxToCh(i):
            return chr(i + ord('a'))
        
        for c1, c2 in zip(s1, s2):
            union(chToIdx(c1), chToIdx(c2))
        for i, p in enumerate(parents):
            parents[i] = find(p)
        return ''.join([idxToCh(parents[chToIdx(c)]) for c in baseStr])