class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]
                if dic[c1] > dic[c2]: return False
                if dic[c1] < dic[c2]: break
                if j + 1 == len(w2) < len(w1): return False
        return True