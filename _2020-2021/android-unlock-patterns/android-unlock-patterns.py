class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        count = 0
        skip = {(1, 3): 2, (4, 6): 5, (7, 9): 8,\
                (1, 7): 4, (2, 8): 5, (3, 9): 6,\
                (1, 9): 5, (3, 7): 5}
        q = deque([[x] for x in range(1, 10)])
        while q:
            path = q.popleft()
            if m <= len(path) <= n: count += 1
            if len(path) > n: continue
            for nxt in range(1, 10):
                if nxt in path: continue
                if ((nxt, path[-1]) in skip and skip[(nxt, path[-1])] not in path)\
                or ((path[-1], nxt) in skip and skip[(path[-1], nxt)] not in path): continue
                q.append(path + [nxt])
        return count