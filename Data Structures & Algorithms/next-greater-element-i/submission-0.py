class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_nums2 = [-1] * len(nums2)
        result_nums1 = [-1] * len(nums1)

        stack = []
        memo = {}

        for curr_index, value in enumerate(nums2):

            memo[value]  = curr_index

            while stack and value > nums2[stack[-1]]:
                result_nums2[stack.pop()] = value 
            
            stack.append(curr_index)

        for curr_index_n1, value in enumerate(nums1):
            if value in memo:
                result_nums1[curr_index_n1] = result_nums2[memo[value]]

        return result_nums1               



        