class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        G = self.buildGraph(pid, ppid)
        ans = []
        q = deque([kill])
        while q:
            cur = q.popleft()
            ans.append(cur)
            for child in G[cur]:
                q.append(child)
        return ans

    def buildGraph(self, pid, ppid):
        G = defaultdict(list)
        for child, parent in zip(pid, ppid):
            G[parent].append(child)
        return G