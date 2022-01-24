class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word += '#'; abbr += '#'
        i, streak = -1, 0
        for ch in abbr:
            if ch.isdigit():
                if streak == 0 and ch == '0': return False
                streak = streak * 10 + int(ch)
            else:
                i += streak + 1
                if i >= len(word) or word[i] != ch: return False
                streak = 0
        return i == len(word)-1                