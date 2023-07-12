class Solution:
    def eventualSafeNodes(self, parentToChildren: List[List[int]]) -> List[int]:
        # keep removing all nodes with indegree == 0
        # in the end all safe nodes will soon or later have indegrees == 0
        childtoParents = defaultdict(list)
        ind = defaultdict(int)
        for parent, children in enumerate(parentToChildren):
            ind[parent] = len(children)
            for child in children:
                childtoParents[child].append(parent)
        q = deque([node for node in ind if ind[node] == 0])
        ans = list(q)
        while q:
            child = q.popleft()
            for parent in childtoParents[child]:
                ind[parent] -= 1
                if ind[parent] == 0:
                    q.append(parent)
                    ans.append(parent)
        return sorted(ans)