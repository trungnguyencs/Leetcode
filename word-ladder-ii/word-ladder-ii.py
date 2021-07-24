class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        q = deque([[beginWord]])
        wordList = set(wordList)
        visited = set()
        foundPath = False
        while q:
            levelVisited = set()
            for _ in range(len(q)):
                path = q.popleft()
                for neigh in self.getNeighbors(path[-1]):
                    if neigh not in wordList or neigh in visited: continue
                    q.append(path + [neigh])
                    levelVisited.add(neigh)
                    if neigh == endWord:
                        foundPath = True
                        ans.append(path + [neigh])
            visited.update(levelVisited)
            if foundPath: break
        return ans
        
    def getNeighbors(self, word):
        neighs = []
        for i, ch in enumerate(word):
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) == ch: continue
                neighs.append(word[:i] + chr(c) + word[i+1:])
        return neighs