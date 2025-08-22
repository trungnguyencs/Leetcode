class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        dic = defaultdict(list)
        phrases = [p.split() for p in phrases]
        ans = set()
        for i, p in enumerate(phrases):
            start, rest = p[0], p[1:]
            dic[start].append((i, rest))
        for i, p in enumerate(phrases):
            end = p[-1]
            for j, rest in dic[end]:
                if i != j:
                    ans.add(' '.join(p + rest))
        return sorted(list(ans))