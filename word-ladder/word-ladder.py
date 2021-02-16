class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        distance = {beginWord: 1}
        q = deque([beginWord])
        while q:
            cur = q.popleft()
            if cur == endWord: return distance[cur]
            for neigh in self.createNeighbors(cur):
                if neigh not in wordList or neigh in distance: continue
                distance[neigh] = distance[cur] + 1
                q.append(neigh)
        return 0
        
    def createNeighbors(self, word):
        neighs = []
        for i, ch in enumerate(word):
            for j in range(ord('a'), ord('z') + 1):
                if chr(j) == ch: continue
                neighs.append(''.join(word[:i] + chr(j) + word[i+1:]))
        return neighs