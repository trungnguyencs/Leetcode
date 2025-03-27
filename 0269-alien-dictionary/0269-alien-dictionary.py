class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #topological sort
        G, ind, charSet, isValid = self.buildGraph(words)
        if not isValid: return ''
        lexico = []
        q = deque([c for c in charSet if ind[c] == 0])
        while q:
            cur = q.popleft()
            if cur not in lexico:
                lexico.append(cur)
            for parent in G[cur]:
                ind[parent] -= 1
                if ind[parent] == 0:
                    q.append(parent)
        lexico.reverse()
        return ''.join(lexico) if len(lexico) == len(charSet) else ''

    def buildGraph(self, words):
        G = defaultdict(list)
        ind = defaultdict(int)
        charSet = set(list(words[0]))
        for i in range(1, len(words)):
            charSet.update(list(words[i]))
            s, e = self.findFirstDifference(words[i-1], words[i])
            if s == 'invalid': return None, None, None, False
            if s != e: #s should appear before e in this alien dictionary
                G[e].append(s)
                ind[s] += 1
        return G, ind, charSet, True

    def findFirstDifference(self, s1, s2):
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return s1[i], s2[i]
        return ('invalid', 'invalid') if len(s1) > len(s2) else (None, None)