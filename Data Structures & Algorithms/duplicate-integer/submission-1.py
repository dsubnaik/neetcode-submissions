class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #declare hash table, using set because we only care about unique
        hash_table=set()

        #loop through and if duplicate is found it breaks and returns 
        #if it isnt in there then it adds to the hashtable/set
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return True
            

            hash_table.add(nums[i])
        
        #returns false if loops end because it is not found
        return False
