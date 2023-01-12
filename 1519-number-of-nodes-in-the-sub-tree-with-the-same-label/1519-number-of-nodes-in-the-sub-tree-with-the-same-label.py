class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        self.ans = [0]*n
        self.postOrder(0, -1, G, labels)
        return self.ans

    def postOrder(self, cur, parent, G, labels):
        ch = labels[cur]
        counter = Counter({ch: 1})
        for child in G[cur]:
            if child == parent: continue
            counter += self.postOrder(child, cur, G, labels)
        self.ans[cur] = counter[ch]
        return counter