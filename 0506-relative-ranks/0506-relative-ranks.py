class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {s: i for i, s in enumerate(sorted(score, reverse=True))}
        ans = []
        for s in score:
            r = rank[s]
            if r == 0:
                ans.append("Gold Medal")
            elif r == 1:
                ans.append("Silver Medal")
            elif r == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(r + 1))
        return ans