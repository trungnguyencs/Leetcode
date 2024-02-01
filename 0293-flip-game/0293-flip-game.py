class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        tmp = list(currentState)
        for i in range(len(tmp) - 1):
            if tmp[i] == tmp[i+1] == '+':
                tmp[i] = tmp[i+1] = '-'
                ans.append(''.join(tmp))
                tmp[i] = tmp[i+1] = '+'
        return ans