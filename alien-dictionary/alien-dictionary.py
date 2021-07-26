class Solution:
    def alienOrder(self, words: List[str]) -> str:
        G, ind, charSet, isValid = self.buildGraph(words)
        if not isValid: return ''
        q = deque([c for c in charSet if ind[c] == 0])
        lexico = []
        while q:
            cur = q.popleft()
            lexico.append(cur)
            for parent in G[cur]:
                ind[parent] -= 1
                if ind[parent] == 0:
                    q.append(parent)
        return ''.join(lexico)[::-1] if len(lexico) == len(charSet) else ''
            
    def buildGraph(self, words):
        G = defaultdict(set)
        ind = defaultdict(int)
        charSet = set(list(words[0]))
        for w in range(1, len(words)):
            prevWord, curWord = words[w-1], words[w]
            m = min(len(prevWord), len(curWord))
            if prevWord[:m] == curWord[:m] and len(prevWord) > len(curWord):
                return G, ind, charSet, False
            for i in range(m):
                parent, child = prevWord[i], curWord[i]
                if parent == child: continue
                if parent in G[child]: break
                if child in G[parent]:
                    return G, ind, charSet, False
                ind[parent] += 1
                G[child].add(parent)
                break
            charSet.update(list(words[w]))
        return G, ind, charSet, True