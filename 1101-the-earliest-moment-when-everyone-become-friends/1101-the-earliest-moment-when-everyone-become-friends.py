class Solution:
    def earliestAcq(self, logs: List[List[int]],  N: int) -> int:
        self.groupCount = N
        self.parents = [i for i in range(N)]
        logs.sort(key=lambda x: x[0])
        for time, x, y in logs:
            if self.union(x, y):
                return time
        return -1
        
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 != parent2:
            self.parents[parent2] = parent1
            self.groupCount -= 1
        return self.groupCount == 1 # return True when all nodes are connected
    
    def find(self, node):
        root = node
        while root != self.parents[root]:
            root = self.parents[root]
        
        # flatten the child -> root path for better perf
        while node != root:
            nextParent = self.parents[node]
            self.parents[node] = root
            node = nextParent
        return root