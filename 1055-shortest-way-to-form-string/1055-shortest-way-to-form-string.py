class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if any(c not in source for c in target): return -1
        count = i = j = 0
        while j < len(target):
            if source[i] == target[j]:
                i += 1
                j += 1
            else:
                i += 1
            if i == len(source):
                i = 0
                count += 1
        return count if i == 0 else count + 1