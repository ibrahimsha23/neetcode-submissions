class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            # If the current number is greater than 0, 
            # three positive numbers cannot sum to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two-pointer search for the remaining two elements
            low, high = i + 1, n - 1
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                
                if three_sum < 0:
                    low += 1
                elif three_sum > 0:
                    high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    
                    # Skip duplicate values for the second element
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                        
                    # Skip duplicate values for the third element
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                        
        return result