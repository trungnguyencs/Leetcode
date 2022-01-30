class Solution:
    def groupStrings(self, words: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in words:
            dic[self.word2Distances(word)].append(word)
        return dic.values()
    
    def word2Distances(self, word):
        distances = [0]
        for i in range(len(word)):
            d = ord(word[i]) - ord(word[i-1])
            distances.append(d if d >= 0 else 26 + d)
        return tuple(distances)