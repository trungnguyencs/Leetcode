class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[self.getFreqArr(s)].append(s)
        return list(dic.values())

    def getFreqArr(self, s):
        arr = [0]*26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        return tuple(arr)