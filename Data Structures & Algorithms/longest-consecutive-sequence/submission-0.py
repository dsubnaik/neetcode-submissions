class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        s=set(nums)
        answer=0

        for i in s:
            if (i-1) not in s:
                
                length=1
                current=i

                while current+1 in s:
                    current+=1
                    length+=1
                
                answer = max(answer, length)

        return answer