class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set([start])
        while q:
            cur = q.popleft()
            if arr[cur] == 0: return True
            for nxt in [cur - arr[cur], cur + arr[cur]]:
                if not 0 <= nxt < len(arr) or nxt in visited:
                    continue
                visited.add(nxt)
                q.append(nxt)
        return False