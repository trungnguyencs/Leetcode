class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        G = defaultdict(list)
        for child, parent in zip(pid, ppid):
            G[parent].append(child)
        ans = []
        q = deque([kill])
        while q:
            cur = q.popleft()
            ans.append(cur)
            q.extend(G[cur])
        return ans