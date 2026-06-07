class Solution:
    def trap(self, height: List[int]) -> int:
        
        sum=0
        left=[]
        right=[]
        
        left_max=0
        right_max=0
        
        for i in range(len(height)):
            
            left.append(left_max)
            
            left_max=max(left_max,height[i])
            
        for i in range(len(height)-1,-1,-1):
            
            right.insert(0, right_max)
            
            right_max=max(right_max,height[i])
            
        for i in range(len(height)):
            
            temp_water=min(left[i],right[i])-height[i]
            
            if temp_water < 0:
                temp_water=0
                
            sum+=temp_water
            
    
        return sum