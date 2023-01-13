class Solution:
    def longestPath(self, parents: List[int], s: str) -> int:
        children = defaultdict(list)
        for c, p in enumerate(parents):
            children[p].append(c)
        self.ans = 1
        self.postOrder(0, children, s)
        return self.ans
        
    def postOrder(self, cur, children, s):
        if not children[cur]:
            return 1
        firstMax = secondMax = 0
        for c in children[cur]:
            pathLen = self.postOrder(c, children, s) #longest path may lie in a subtree so cannot skip even if same char as root
            if s[c] == s[cur]: continue
            if pathLen >= firstMax:
                firstMax, secondMax = pathLen, firstMax
            elif pathLen > secondMax:
                secondMax = pathLen
        self.ans = max(self.ans, firstMax + secondMax + 1)
        return firstMax + 1