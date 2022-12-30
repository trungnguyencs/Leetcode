class Solution:
    def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
        ans = []
        q = deque([[0]])
        while q:
            path = q.popleft()
            for neigh in G[path[-1]]:
                newPath = path + [neigh]
                if neigh == len(G) - 1:
                    ans.append(newPath)
                else:
                    q.append(newPath)
        return ans