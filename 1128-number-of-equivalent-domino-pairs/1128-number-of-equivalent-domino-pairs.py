class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = Counter()
        ans = 0
        for a, b in dominoes:
            if (a, b) in counter:
                ans += counter[(a, b)]
                counter[(a, b)] += 1
            elif (b, a) in counter:
                ans += counter[(b, a)]
                counter[(b, a)] += 1
            else:
                counter[(a, b)] = 1
        return ans