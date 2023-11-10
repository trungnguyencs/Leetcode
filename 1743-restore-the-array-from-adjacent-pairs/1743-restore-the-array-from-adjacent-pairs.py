class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for a, b in adjacentPairs:
            G[a].append(b)
            G[b].append(a)
        for start in G:
            if len(G[start]) == 1:
                ans = [start, G[start][0]]
        while len(G[ans[-1]]) != 1:
            cur, prev = ans[-1], ans[-2]
            for nxt in G[cur]:
                if nxt != prev:
                    ans.append(nxt)
        return ans