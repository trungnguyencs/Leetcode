class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {ch: i for i, ch in enumerate(keyboard)}
        return dic[word[0]] + sum(abs(dic[word[i]] - dic[word[i-1]]) for i in range(1, len(word)))