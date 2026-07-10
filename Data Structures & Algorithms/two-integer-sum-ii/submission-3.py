class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1

        res = []

        while l < h:

            if numbers[l] + numbers[h] > target:
                h -= 1
            elif numbers[l] + numbers[h] < target:
                l += 1
            else:
                print(l, h)
                res = [l+1, h+1]
                return res
        return res



            
        