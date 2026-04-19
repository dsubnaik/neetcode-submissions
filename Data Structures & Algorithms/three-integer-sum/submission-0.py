class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        answer=[]
        nums=sorted(nums)
        
        #print(nums)
        
        for i in range(len(nums)):
            low=i+1
            high=len(nums)-1
            
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
                
            if nums[i] > 0:
                    break
            
            while low<high:
                triplet_sum=nums[i]+nums[low]+nums[high]
                
                 
                
                if triplet_sum == 0:
                    answer.append([nums[i],nums[low],nums[high]])
                    
                    low += 1
                    high -= 1
                    
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                        
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                        
                        
                elif triplet_sum <0:
                    low +=1
                else:
                    high-=1
                
        return answer
        