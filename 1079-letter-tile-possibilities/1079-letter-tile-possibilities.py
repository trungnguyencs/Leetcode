class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.uniqueSequences = set()
        self.backtrack([], set(), 0, tiles)
        return len(self.uniqueSequences) - 1

    def backtrack(self, arr, visited, i, tiles):
        if i == len(tiles):
            self.uniqueSequences.add(''.join(arr))
            return
        self.backtrack(arr, visited, i + 1, tiles)
        for j, ch in enumerate(tiles):
            if j in visited: continue
            visited.add(j)
            self.backtrack(arr + [ch], visited, i + 1, tiles)
            visited.remove(j)