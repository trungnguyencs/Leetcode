class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        tripleACount = tripleBCount = 0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] == colors[i+1] == 'A':
                tripleACount += 1
            elif colors[i-1] == colors[i] == colors[i+1] == 'B':
                tripleBCount += 1
        return tripleACount > tripleBCount