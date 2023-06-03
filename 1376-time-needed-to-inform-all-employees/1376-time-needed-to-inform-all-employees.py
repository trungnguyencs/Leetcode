class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = defaultdict(list)
        for employee, manager in enumerate(manager):
            dic[manager].append(employee)
        return self.dfs(headID, dic, informTime)
    
    def dfs(self, manager, dic, informTime):
        if not dic[manager]:
            return 0
        return informTime[manager] + max(self.dfs(child, dic, informTime) for child in dic[manager])