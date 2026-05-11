class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #create dictionary default as list to store solution
        result=defaultdict(list)
        
        #loup through each string
        for i in range(len(strs)):
            
            #create array with corresponding alphabet which is 26 letters
            count=[0]*26
            
            #get counts of string
            for j in strs[i]:
                
                #using asci characters so ex a i think is 80,b would 81 81-80 would increase b(index 1) by 1
                count[ord(j)-ord("a")]+=1
                
            #append the string into list
            result[tuple(count)].append(strs[i])
            
        
        return list(result.values())