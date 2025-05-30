class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        G = self.buildGraph(edges)
        q1, q2 = deque([node1]), deque([node2])
        visited1, visited2 = set([node1]), set([node2])
        while q1 or q2:
            ans = []
            tmp1 = []
            tmp2 = []
            for _ in range(len(q1)):
                cur1 = q1.pop()
                if cur1 in visited2:
                    ans.append(cur1)
                for neigh in G[cur1]:
                    if neigh not in visited1:
                        tmp1.append(neigh) #add directly to visited1 might affect line 20 and not return the smallest index
                        q1.append(neigh)
            for _ in range(len(q2)):
                cur2 = q2.pop()
                if cur2 in visited1:
                    ans.append(cur2)
                for neigh in G[cur2]:
                    if neigh not in visited2:
                        tmp2.append(neigh)
                        q2.append(neigh)
            visited1.update(tmp1)
            visited2.update(tmp2)
            if ans: return min(ans)
        return -1

    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in enumerate(edges):
            if e != -1:
                G[s].append(e)
        return G