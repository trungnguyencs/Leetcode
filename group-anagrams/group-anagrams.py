class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[self.toCounter(s)].append(s)
        return dic.values()
        
    def toCounter(self, s):
        counter = [0]*26
        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        return tuple(counter)