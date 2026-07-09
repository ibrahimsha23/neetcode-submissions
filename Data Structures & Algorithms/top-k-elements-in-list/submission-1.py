class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mapCounter = {}
        bucket = [None] * (len(nums) + 1)

        for num in nums:
            if mapCounter.get(num):
                mapCounter[num] += 1
            else:
                mapCounter[num] = 1
        
        print(mapCounter, )
        for key, value in mapCounter.items():
            if not bucket[value]:
                bucket[value] = [key]
            else:
                bucket[value].append(key)

        result = []
        counter = 0
        
        for ele_bucket in bucket[::-1]:
            print(ele_bucket)
            if ele_bucket is None:
                continue
            else:
                for ele in ele_bucket:
                    if len(result) < k:
                        result.append(ele)
        return result







        

         

        