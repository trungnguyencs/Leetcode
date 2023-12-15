class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set(path[0] for path in paths)
        for _, e in paths:
            if e not in src: return e