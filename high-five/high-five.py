class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        records = defaultdict(list)
        for id, score in items:
            heap = records[id]
            if len(heap) < 5: heappush(heap, score)
            elif len(heap) == 5 and heap[0] < score: heapreplace(heap, score)
        return [[id, sum(records[id])//len(records[id])] for id in sorted(records.keys())]