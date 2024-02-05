class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {w:i for i, w in enumerate(list1)}
        dic2 = {w:i for i, w in enumerate(list2)}
        minSum = float('inf')
        ans = []
        for w in dic1:
            if w in dic2:
                s = dic1[w] + dic2[w]
                if s == minSum: 
                    ans.append(w)
                elif s < minSum:
                    minSum = s
                    ans = [w]
        return ans