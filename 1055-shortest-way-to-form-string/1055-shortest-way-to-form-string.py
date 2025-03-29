class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        #using 2 pointers on Source and Target would take O(T * S)
        #instead, build a hashmap of increasing indexes for each char in Source
        #then binary search on that list -> overall O(S + TlogS)
        dic = defaultdict(list)
        for i, ch in enumerate(source):
            dic[ch].append(i)
        prevIdx = -1
        ans = 1
        print(dic)
        for ch in target:
            if ch not in dic: return -1
            i = bisect_left(dic[ch], prevIdx + 1)
            if i == len(dic[ch]): #move to start of source again
                ans += 1
                prevIdx = dic[ch][bisect_left(dic[ch], 0)]
            else:
                prevIdx = dic[ch][i]
        return ans

        #further optimization:
        #example: let source = 'abacad'
        #instead of having dic['a'] = [0, 2, 4], we can have dic['a'] = [0, 2, 2, 4, 4, -1] (length == len(source))
        #that way we can look up the index in O(1) instead of binary search O(log(len(source)))