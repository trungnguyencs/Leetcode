class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        first, second, third = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        for word in words:
            line = self.getLine(word[0], first, second, third)
            satisfy = True
            for i in range(1, len(word)):
                if self.getLine(word[i], first, second, third) == line: continue
                satisfy = False
                break
            if satisfy: ans.append(word)
        return ans
    
    def getLine(self, ch, first, second, third):
        ch = ch.lower()
        return 1 if ch in first else 2 if ch in second else 3