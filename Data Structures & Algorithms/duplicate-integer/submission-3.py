class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set_container = set()
        for num in nums:
            num_set_container.add(num) 
        return len(num_set_container) != len(nums)
        
        