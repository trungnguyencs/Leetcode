class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        #this is equivalent to finding the most common pattern
        #I.e. 100100 and 011011 have the same pattern
        counter = Counter()
        for row in matrix:
            code = tuple([row[i] == row[0] for i in range(1, len(row))])
            counter[code] += 1
        return max(counter.values())