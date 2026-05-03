class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_table={}
        
        for i in range(len(nums)):
    
            difference=target-nums[i]
            
            if difference in hash_table:
                return ([hash_table[difference],i])
            
            if nums[i] not in hash_table:
                hash_table[nums[i]]=i