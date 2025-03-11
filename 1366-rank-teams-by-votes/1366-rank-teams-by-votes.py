class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dic = {}
        for vote in votes:
            for i, ch in enumerate(vote):
                if ch not in dic:
                    dic[ch] = [0]*26
                dic[ch][i] -= 1
        ans = list(votes[0])
        ans.sort(key=lambda ch: (dic[ch], ch))
        return ''.join(ans)