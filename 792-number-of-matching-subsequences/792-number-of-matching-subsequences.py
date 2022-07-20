class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list)
        for i, ch in enumerate(s):
            dic[ch].append(i)
        return sum(self.isSubsequence(w, dic) for w in words)
        
    def isSubsequence(self, w, dic): # binary search solution
        prevIndex = -1
        for ch in w:
            lst = dic[ch]
            i = bisect_left(lst, prevIndex + 1)
            if i == len(lst): return False
            prevIndex = lst[i]
        return True