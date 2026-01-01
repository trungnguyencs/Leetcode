from sortedcontainers import SortedList

class Leaderboard:

    def __init__(self):
        self.list = SortedList()
        self.dic = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        # O(logN)
        if self.dic[playerId] > 0:
            oldScore = self.dic[playerId]
            newScore = oldScore + score
            self.dic[playerId] = newScore
            self.list.remove(oldScore)
            self.list.add(newScore)
        else:
            self.dic[playerId] = score
            self.list.add(score)

    def top(self, K: int) -> int:
        # O(KlogN)
        return sum(self.list[-K:])

    def reset(self, playerId: int) -> None:
        # O(logN)
        score = self.dic[playerId]
        self.list.remove(score)
        del self.dic[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)