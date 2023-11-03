class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        operations = []
        for num in range(1, n + 1):
            if num == target[i]:
                operations.append("Push")
                i += 1
                if i == len(target): break
            else:
                operations.extend(["Push", "Pop"])
        return operations    