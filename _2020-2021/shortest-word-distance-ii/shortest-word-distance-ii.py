class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.dic[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        idxList1, idxList2 = self.dic[word1], self.dic[word2]
        i, j = 0, 0
        minDistance = float('inf')
        while i < len(idxList1) and j < len(idxList2):
            idx1, idx2 = idxList1[i], idxList2[j]
            minDistance = min(minDistance, abs(idx1 - idx2))
            if idx1 < idx2:
                i += 1
            else:
                j += 1
        return minDistance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)