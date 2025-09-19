from sortedcontainers import SortedList

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.list = SortedList()
        self.dic = {}
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.list.add((priority, taskId))
        self.dic[taskId] = userId, priority

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.dic[taskId]
        self.dic[taskId] = (userId, newPriority)
        self.list.remove((priority, taskId))
        self.list.add((newPriority, taskId))

    def rmv(self, taskId: int) -> None:
        userId, priority = self.dic[taskId]
        del self.dic[taskId]
        self.list.remove((priority, taskId))

    def execTop(self) -> int:
        if not self.list:
            return -1
        taskId = self.list[-1][1]
        userId, priority = self.dic[taskId]
        del self.dic[taskId]
        self.list.remove((priority, taskId))
        return userId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()