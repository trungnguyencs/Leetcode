class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        G = defaultdict(list)
        for parent, child in zip(ppid, pid):
            G[parent].append(child)
        ans = [kill]
        q = deque([kill])
        while q:
            cur = q.popleft()
            for child in G[cur]:
                q.append(child)
                ans.append(child)
        return ans
