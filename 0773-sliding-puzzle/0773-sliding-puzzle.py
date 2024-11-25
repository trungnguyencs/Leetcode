class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dest = [1, 2, 3, 4, 5, 0]
        neighs = {0: [1, 3],
                  1: [0, 2, 4],
                  2: [1, 5],
                  3: [0, 4],
                  4: [1, 3, 5],
                  5: [2, 4]}
        board = board[0] + board[1]
        q = deque([(board, board.index(0))])
        visited = set(tuple(board))
        step = 0
        while q:
            for _ in range(len(q)):
                cur, i = q.popleft()
                if cur == dest: return step
                for j in neighs[i]:
                    nxt = cur[:]
                    nxt[i], nxt[j] = nxt[j], nxt[i]
                    if tuple(nxt) in visited: continue
                    q.append([nxt, j])
                    visited.add(tuple(nxt))
            step += 1
        return -1