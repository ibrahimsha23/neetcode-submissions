class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1


        while not left > right:

            if left == right:
                return True
            
            l_str = s[left]
            r_str = s[right]


            if not l_str.isalnum() or l_str.isspace():
                left += 1
                continue

            if not r_str.isalnum() or  r_str.isspace():
                right -= 1
                continue

            if l_str.lower() != r_str.lower():
                return False
            
            left += 1
            right -= 1


        return True 




        