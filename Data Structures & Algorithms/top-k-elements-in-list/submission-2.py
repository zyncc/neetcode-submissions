import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        result = []

        for num, count in counter.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
            
        for i in range(len(heap)):
            count, num = heap[i]
            result.append(num)

        return result
