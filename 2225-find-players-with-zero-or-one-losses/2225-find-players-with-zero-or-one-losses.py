class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseCounter = Counter()
        for winner, loser in matches:
            if winner not in loseCounter: loseCounter[winner] = 0
            loseCounter[loser] += 1
        noLose = [player for player, loseCount in loseCounter.items() if loseCount == 0]
        oneLose = [player for player, loseCount in loseCounter.items() if loseCount == 1]
        return [sorted(noLose), sorted(oneLose)]