class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            encoded += s

        return encoded



    def decode(self, s: str) -> List[str]:
        print(s)
        n = len(s) 
        decoded = []
        index = 0
        end = 0
        while index < n:
            
            end_prefix_string = ""
            while s[index] != "#":
                
                end_prefix_string += s[index]
                index += 1
            end = int(end_prefix_string)
            
            
            index += 1 # skip #

            temp = s[index:index+end]
            decoded.append(temp)
            index += end 
        return decoded













        