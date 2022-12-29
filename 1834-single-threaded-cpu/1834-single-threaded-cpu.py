class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = sorted([(enqueTime, processingTime, i) for i, (enqueTime, processingTime) in enumerate(tasks)])
        curTime = j = 0
        heap, ans = [], []
        while heap or j < len(arr):
            if not heap and curTime < arr[j][0]:
                curTime = arr[j][0]
            while j < len(arr) and curTime >= arr[j][0]:
                heappush(heap, (arr[j][1], arr[j][2]))
                j += 1
            processingTime, i = heappop(heap)
            curTime += processingTime
            ans.append(i)
        return ans