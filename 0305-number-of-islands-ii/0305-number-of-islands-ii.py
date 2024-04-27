class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        union = UnionFind()
        for r, c in positions:
            if (r, c) in union.id:
                ans.append(union.componentCount)
                continue
            union.add((r, c))
            neighs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in neighs:
                if (nr, nc) in union.id:
                    union.union((nr, nc), (r, c))
            ans.append(union.componentCount)
        return ans
    
class UnionFind:
    def __init__(self):
        self.id = {}
        self.size = {}
        self.componentCount = 0
        
    def add(self, x):
        self.id[x] = x
        self.size[x] = 1
        self.componentCount += 1
    
    def find(self, x):
        while x != self.id[x]:
            self.id[x] = self.id[self.id[x]]
            x = self.id[x]
        return x
        
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.size[x] < self.size[y]:
            x, y = y, x
        # add the smaller component as subtree of the bigger component
        self.id[y] = x
        self.size[x] += self.size[y]
        self.componentCount -= 1