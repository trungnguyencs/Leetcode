class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if len(words) != len(max(words, key=len)): return False
        for r in range(len(words)):
            for c in range(len(words)):
                if c >= len(words[r]) and r >= len(words[c]): continue
                if c >= len(words[r]) or r >= len(words[c]) or words[r][c] != words[c][r]: return False
        return True