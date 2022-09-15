class Solution:
    def findOriginalArray(self, arr: List[int]) -> List[int]:
        counter = Counter(arr)
        for x in sorted(counter.keys()):
            if x == 0:
                if counter[x] % 2 == 1: return []
                counter[x] //= 2
            elif counter[x] > counter[2*x]: return []
            else:
                counter[2*x] -= counter[x]
        return counter.elements()