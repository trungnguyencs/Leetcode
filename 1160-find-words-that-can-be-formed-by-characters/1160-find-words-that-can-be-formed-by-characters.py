class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = Counter(chars)
        return sum(len(w) for w in words if self.canBuildFromDic(w, dic))
        
    def canBuildFromDic(self, word, dic):
        counter = Counter()
        for ch in word:
            counter[ch] += 1
            if counter[ch] > dic[ch]: return False
        return True