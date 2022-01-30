class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strings:
            diff = [0]
            for i in range(len(s) - 1):
                diff.append(self.getDiffWarpedAround(s[i+1], s[i]))
            dic[tuple(diff)].append(s)
        return dic.values()
    
    def getDiffWarpedAround(self, ch1, ch2):
        ascii1, ascii2 = ord(ch1), ord(ch2)
        return ascii2 - ascii1 if ascii2 >= ascii1 else 26 + ascii2 - ascii1