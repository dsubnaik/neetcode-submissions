class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        my_set=set()
        longest_substring=0
        left=0
        right=0
        
        while right<len(s):
            
            if s[right] not in my_set:
                
                my_set.add(s[right])
                right+=1
            
            else:

                my_set.discard(s[left])
                left+=1
    
            longest_substring=max(longest_substring,(right-left))
        
        return longest_substring