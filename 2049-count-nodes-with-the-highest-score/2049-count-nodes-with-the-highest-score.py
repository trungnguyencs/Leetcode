class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.n = len(parents)
        self.maxProd = self.ans = 0
        G = self.buildTree(parents)
        self.postorder(0, G)
        return self.ans

    def postorder(self, root, G):
        children = G[root]
        left = self.postorder(children[0], G) if len(children) >= 1 else 0
        right = self.postorder(children[1], G) if len(children) >= 2 else 0
        prod = (left or 1) * (right or 1) * (self.n - left - right - 1 or 1)
        if prod == self.maxProd:
            self.ans += 1
        elif prod > self.maxProd:
            self.maxProd = prod
            self.ans = 1
        return left + right + 1

    def buildTree(self, parents):
        G = defaultdict(list)
        for child, parent in enumerate(parents):
            G[parent].append(child)
        return G