class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = collections.deque([(0, [0])])
        ans = []
        while q:
            cur, path = q.popleft()
            for neigh in graph[cur]:
                if neigh == len(graph) - 1:
                    ans.append(path[:] + [neigh])
                else:
                    q.append((neigh, path[:] + [neigh]))
        return ans
