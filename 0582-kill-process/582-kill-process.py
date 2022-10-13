class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        G = defaultdict(list)
        for node, parent in zip(pid, ppid):
            G[parent].append(node)
        ans = [kill]
        q = deque([kill])
        while q:
            cur = q.popleft()
            q.extend(G[cur])
            ans.extend(G[cur])
        return ans