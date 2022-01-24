class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        G = self.buildGraph(tickets)
        ans, stack = [], ['JFK']
        while stack:
            cur = stack[-1]
            if not G[cur]:
                ans.append(stack.pop())
            else:
                cur = G[cur].pop()
                stack.append(cur)
        return ans[::-1]
            
    def buildGraph(self, tickets):
        G = defaultdict(list)
        for s, e in tickets:
            G[s].append(e)
        for k in G:
            G[k].sort(reverse=True)
        return G
