class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        counter = Counter(str(n))
        return any(counter == Counter(str(1 << i)) for i in range(31)) 