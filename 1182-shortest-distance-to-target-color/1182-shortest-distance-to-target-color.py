class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i, color in enumerate(colors):
            dic[color].append(i)
        return [self.answerQuery(idx, c, dic) for idx, c in queries]
    
    def answerQuery(self, idx, c, dic):
        lst = dic[c]
        if not lst: return -1
        i = bisect_left(lst, idx)
        if i == 0: return lst[0] - idx
        if i == len(lst): return idx - lst[-1]
        return min(abs(lst[i] - idx), abs(lst[i-1] - idx))