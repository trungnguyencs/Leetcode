class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        dic = defaultdict(set)
        for w1, w2 in similarPairs:
            dic[w1].add(w2)
            dic[w2].add(w1)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2 or w2 in dic[w1]: continue
            return False
        return True