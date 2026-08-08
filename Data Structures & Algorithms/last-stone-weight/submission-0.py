import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            firstLargest = heapq.heappop(heap) * -1
            secondLargest = heapq.heappop(heap) * -1

            difference = firstLargest - secondLargest

            if difference > 0:
                heapq.heappush(heap, difference * -1)

        if len(heap) >= 1:
            return heap[0] * -1
        else: return 0