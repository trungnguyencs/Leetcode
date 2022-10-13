class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        encodedPattern = self.encode(pattern)
        return [w for w in words if self.encode(w) == encodedPattern]
        
    def encode(self, s):
        dic = {}
        encode = []
        for ch in s:
            if ch not in dic:
                dic[ch] = len(dic)
            encode.append(dic[ch])
        return encode