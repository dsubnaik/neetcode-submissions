class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string = ""
        
        for s in strs:
            
            # store: length#string
            encoded_string += str(len(s)) + "#" + s
            
        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        decoded_array = []
        
        count = 0
        
        while count < len(s):
            
            # find the #
            j = count
            
            while s[j] != '#':
                j += 1
            
            # length before #
            length = int(s[count:j])
            
            # extract the string
            word = s[j+1 : j+1+length]
            
            decoded_array.append(word)
            
            # move pointer to next encoded word
            count = j + 1 + length
        
        return decoded_array