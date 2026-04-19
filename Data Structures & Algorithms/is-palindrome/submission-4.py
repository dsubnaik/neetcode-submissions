class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #print(s)
        begin=0
        end=len(s)-1
        
        while begin<=end:
            if not s[begin].isalnum():
                begin+=1
                continue

            if not s[end].isalnum():
                end-=1
                continue
            
            if s[begin].lower() != s[end].lower():
                return False
                
            begin+=1
            end-=1
        
        return True