class Solution:
    def isPalindrome(self, s: str) -> bool:

        # print(len(s))
        my_string=""
        for i in range(len(s)):
            if (s[i].isalnum()):
                my_string+=s[i]
        
        my_string=my_string.lower()
        #print(my_string)

        #for iterating through loop going to use length-1
        length=len(my_string)-1

        for i in range(len(my_string)//2):
            if my_string[i]!=my_string[length]:
               return False
            length-=1
            
        return True   