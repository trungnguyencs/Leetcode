class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.dic = defaultdict(set)
        for word in words:
            self.dic[len(word)].add(word)
        return max(self.dp(word) for word in words)
        
    @cache
    def dp(self, word):
        if len(word) == 1: return 1
        maxSeq = 1
        for prevWord in self.dic[len(word) - 1]:
            if self.canInsertOneChar(prevWord, word):
                maxSeq = max(maxSeq, 1 + self.dp(prevWord))
        return maxSeq
        
    def canInsertOneChar(self, short, long):
        if len(long) != len(short) + 1: return False
        hasDiff = False
        i = j = 0
        while i < len(short):
            if short[i] != long[j]:
                if hasDiff: return False
                hasDiff = True
                j += 1
            else:
                i += 1
                j += 1
        return True