class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        visited[0] = True
        q = deque([0])
        while q:
            cur = q.popleft()
            for neigh in rooms[cur]:
                if visited[neigh]: continue
                visited[neigh] = True
                q.append(neigh)
        return sum(visited) == len(rooms)