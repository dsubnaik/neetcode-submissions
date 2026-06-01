class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #initialize set with nums in it 
        my_set=set(nums)
        longest=0

        
        for n in nums:
            
            #checks if left neighbor exists, whether it is the beginning of a sequence
            if (n-1) not in my_set:
                length=0
                
                #calculates length
                while (n+length) in my_set:
                    length+=1
                    
                longest=(max(longest,length))#replaces longest if current length is longer
            
        return longest