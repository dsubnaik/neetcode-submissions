class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        hash_table = {}

        for i in range(len(nums)):
            #print(nums[i])

            if nums[i] in hash_table:
                hash_table[nums[i]] += 1
            else:
                hash_table[nums[i]] = 1

            #print(hash_table)

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in hash_table.items():
            
            bucket[value].append(key)

        res = []
         
        for i in range(len(bucket) - 1, 0, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])

                if len(res) == k:
                    return res