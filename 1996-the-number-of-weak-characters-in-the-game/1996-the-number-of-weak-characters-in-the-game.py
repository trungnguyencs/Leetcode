class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1])) # x[1] sorted asc because if x[0] == y[0] it should not count
        count, curMax = 0, float('-inf')
        for _, x in properties:
            if x < curMax:
                count += 1
            else:
                curMax = x
        return count