class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        begin=0
        end=len(nums)-1
        
        
        while begin<=end:
            
            middle=(begin+end)//2
            
            if nums[middle]==target:
                return middle
            elif target>nums[middle]:
                begin=middle+1
            else:
                end=middle-1

        return -1