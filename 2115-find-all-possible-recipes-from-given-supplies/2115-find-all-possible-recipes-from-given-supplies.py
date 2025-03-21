class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        G, ind = self.buildGraph(recipes, ingredients)
        q = deque()
        for s in supplies:
            ind[s] = 0
            q.append(s)
        ans = []
        recipeSet = set(recipes)
        while q:
            cur = q.popleft()
            if cur in recipeSet:
                ans.append(cur)
            for parent in G[cur]:
                ind[parent] -= 1
                if ind[parent] == 0:
                    q.append(parent)
        return ans

    def buildGraph(self, recipes, reqs):
        G = defaultdict(list)
        ind = defaultdict(int)
        for parent, req in zip(recipes, reqs):
            for child in req:
                ind[parent] += 1
                G[child].append(parent)
        return G, ind