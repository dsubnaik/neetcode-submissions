class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_array=[1]*len(nums)
        right_array=[1]*len(nums)
        
        left_total=1
        right_total=1
        answer=[]
        
        for i in range(1, len(nums)):
            
            left_total*=nums[i-1]
            left_array[i]=left_total
            
        
        for i in reversed(range(len(nums)-1)):
            right_total *= nums[i+1]
            right_array[i] = right_total
        
        
        for i in range(len(nums)):
            
            answer.append(right_array[i]*left_array[i])
            
        return answer