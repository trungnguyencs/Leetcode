class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        dic = {}
        for i, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = i
            else:
                dic[ch] = len(s)
        ret = min(dic.values())
        return ret if ret != len(s) else -1