class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        lst, word = [], []
        for i, ch in enumerate(s):
            if ch != ' ':
                word.append(ch)
            if word and (ch == ' ' or i == len(s)-1):
                lst.append(''.join(word))
                word = []
        return ' '.join(reversed(lst))