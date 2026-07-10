class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        

        freq_mapper = {}
        count = 1
        res = 1

        for num in nums:
            if freq_mapper.get(num):
                freq_mapper[num] = True
            else:
                freq_mapper[num] = True
        
        for num in nums:

            stepper = 1

            while freq_mapper.get(num + stepper, False):
                count += 1
                stepper += 1
            
            res = max(count, res)
            count = 1
        return res



        