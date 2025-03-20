class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word, abbr = word + '#', abbr + '#'
        i = streak = 0
        for ch in abbr:
            if ch.isdigit():
                if ch == '0' and streak == 0: return False
                streak = streak * 10 + int(ch)
            else:
                i, streak = i + streak, 0
                if i >= len(word) or word[i] != ch: return False
                i += 1
        return i == len(word)