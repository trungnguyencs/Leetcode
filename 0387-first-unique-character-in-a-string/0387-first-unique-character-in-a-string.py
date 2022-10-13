class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, ch in enumerate(s):
            if ch in dic:
                dic[ch] = len(s)
            else:
                dic[ch] = i
        minIndex = min(dic.values())
        return -1 if minIndex == len(s) else minIndex
        