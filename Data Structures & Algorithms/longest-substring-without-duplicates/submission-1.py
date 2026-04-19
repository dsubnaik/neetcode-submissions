class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        my_set=set()
        longest=0
        l=0
        r=0
        
        while r<len(s):
            if s[r] not in my_set:
                my_set.add(s[r])
                
                r+=1
                if longest<r-l:
                    longest=r-l
            else:
                while s[r] in my_set:
                    my_set.remove(s[l])
                    l+=1
                    
            
        return longest