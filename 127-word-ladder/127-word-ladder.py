class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDic = set(wordList)
        q = deque([beginWord])
        visited = {beginWord: 1}
        while q:
            cur = q.popleft()
            for neigh in self.getNeighbors(cur, wordDic):
                if neigh in visited: continue
                if neigh == endWord: return visited[cur] + 1
                visited[neigh] = visited[cur] + 1
                q.append(neigh)
        return 0
    
    def getNeighbors(self, word, wordDic):
        neighs = []
        for i, ch in enumerate(word):
            for j in range(ord('a'), ord('z') + 1):
                newCh = chr(j)
                newWord = word[:i] + newCh + word[i+1:]
                if newCh != ch and newWord in wordDic:
                    neighs.append(newWord)
        return neighs