class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashtable={}

        for i in range(len(strs)):
            count = [0]*26

            for j in strs[i]:
                index= ord(j)-ord('a')
                count[index]+=1

            key = tuple(count)

            if key not in hashtable:
                hashtable[key]=[]

            hashtable[key].append(strs[i])

        return list(hashtable.values())

        