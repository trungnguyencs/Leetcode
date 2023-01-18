# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        return self.helper(reader, 0, reader.length() - 1)
        
    def helper(self, reader, l, r):
        m = (l + r)//2
        if l == m == r: return l
        if l == m != r: return l if reader.compareSub(l, l, r, r) == 1 else r
        if (r - l + 1) % 2 == 0: # even count
            return self.helper(reader, l, m) if reader.compareSub(l, m, m+1, r) == 1 else self.helper(reader, m + 1, r)
        # odd count
        cmp = reader.compareSub(l, m-1, m+1, r)
        return m if cmp == 0 else self.helper(reader, l, m-1) if cmp == 1 else self.helper(reader, m+1, r)