class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        #just do a hashmap and find the smallest element that appears n times
        #doing dolumn by colum from left to right so that we can exit early
        counter = Counter()
        for c in range(len(mat[0])):
            for row in mat:
                num = row[c]
                counter[num] += 1
                if counter[num] == len(mat):
                    return num
        return -1