import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mapCounter = {}
        bucket = [None] * (len(nums) + 1)

        for num in nums:
            if mapCounter.get(num):
                mapCounter[num] += 1
            else:
                mapCounter[num] = 1
        
        heap = []
        for key, value in mapCounter.items():

            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
        return [ num for count, num in heap]








        

         

        