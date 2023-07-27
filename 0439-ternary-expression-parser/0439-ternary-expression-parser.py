class Solution:
    def parseTernary(self, s: str) -> str:
        if len(s) == 1: return s
        qIdx = self.findLastQuestionMarkIdx(s)
        cIdx = self.findNextColonIdx(s, qIdx)
        ans = s[cIdx - 1] if s[qIdx - 1] == 'T' else s[cIdx + 1]
        return self.parseTernary(s[:qIdx - 1] + ans + s[cIdx + 2:])
        
    def findLastQuestionMarkIdx(self, s):
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '?': return i
    
    def findNextColonIdx(self, s, questionMarkIdx):
        for i in range(questionMarkIdx + 1, len(s)):
            if s[i] == ':': return i