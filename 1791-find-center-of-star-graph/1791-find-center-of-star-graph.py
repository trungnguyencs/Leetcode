class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s, e = edges[0]
        if s in edges[1]: return s
        if e in edges[1]: return e