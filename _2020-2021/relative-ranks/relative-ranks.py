class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        scoresCopy = sorted(copy.deepcopy(scores), reverse=True)
        dic = {score: rank for rank, score in enumerate(scoresCopy)}
        ans = []
        for score in scores:
            rank = dic[score]
            ans.append("Gold Medal" if rank == 0 else "Silver Medal" if rank == 1 else "Bronze Medal" if rank == 2 else str(rank + 1))
        return ans