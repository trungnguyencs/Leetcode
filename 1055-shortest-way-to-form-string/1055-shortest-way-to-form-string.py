class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        dic = defaultdict(list)
        for i, ch in enumerate(source):
            dic[ch].append(i)
        count = i = 0
        for ch in target:
            if ch not in dic: return -1
            j = bisect_left(dic[ch], i)
            if j == len(dic[ch]):
                i = dic[ch][bisect_left(dic[ch], 0)] + 1
                count += 1
            else:
                i = dic[ch][j] + 1
        return count + 1