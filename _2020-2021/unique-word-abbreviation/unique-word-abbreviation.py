class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = defaultdict(set)
        for w in dictionary:
            abbr = w[0], len(w), w[-1]
            self.dic[abbr].add(w)

    def isUnique(self, w: str) -> bool:
        abbr = w[0], len(w), w[-1]
        return not self.dic[abbr] or self.dic[abbr] == {w}

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)