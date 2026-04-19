class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        #everything to the left
        left=1
        left_array=[]
        for i in range(len(nums)):
            left_array.append(left)
            left*=nums[i]
            #print(left_array)
        

        #everything to the right
        right=1
        right_array=[]
        for i in range((len(nums)-1),-1,-1):
            #print(i)
            right_array.append(right)
            right*=nums[i]
            #print(right_array)


        right_array.reverse()

        #print(right_array)

        #multiply to get solution
        solution=[]
        for i in range(len(nums)):
            solution.append(left_array[i]*right_array[i])
            #print(solution)

        return solution