class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = {tuple(start): 0}
        heap = [(0, start)]
        ans = float('inf')
        #heap isn't better than queue because there's a case
        #where it's the shortest so far but the last segment is so long it becomes not shortest overall
        #so we still need to pop till heap/queue is empty
        while heap:
            d, cur = heappop(heap)
            if cur == tuple(destination):
                ans = min(ans, d)
            r, c = cur
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc, nd = r, c, d
                while 0 <= nr + dr < len(maze) and 0 <= nc + dc < len(maze[0]) and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    nd += 1
                if (nr, nc) not in visited or visited[(nr, nc)] > nd:
                    visited[(nr, nc)] = nd
                    heappush(heap, (nd, (nr, nc)))
        return ans if ans != float('inf') else -1