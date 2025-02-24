class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        #use BFS or DFS to find the path for Bob to get to root
        #from that path to root: 1st half update all values to 0, middle node update to val//2, later half no change
        #use dfs to find the max path for Alice
        G = self.buildGraph(edges)
        bobPath = self.findBobPath(G, bob)
        self.updateAmount(bobPath, amount)
        return self.findMaxPath(0, G, set(), amount)

    def findBobPath(self, G, bob):
        q = deque([(bob, [bob])])
        visited = set([bob])
        while q:
            cur, path = q.popleft()
            if cur == 0:
                rootPath = path
                return path
            for neigh in G[cur]:
                if neigh in visited: continue
                q.append((neigh, path + [neigh]))
                visited.add(neigh)

    def updateAmount(self, bobPath, amount):
        for i in range(len(bobPath)//2):
            amount[bobPath[i]] = 0
        if len(bobPath) % 2 == 1:
            middleNode = bobPath[len(bobPath)//2]
            amount[middleNode] //= 2
         
    def findMaxPath(self, root, G, visited, amount):
        visited.add(root)
        maxPath = float('-inf')
        for neigh in G[root]:
            if neigh in visited: continue
            maxPath = max(maxPath, self.findMaxPath(neigh, G, visited, amount))
        return amount[root] + maxPath if maxPath != float('-inf') else amount[root]

    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G