class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s,t)
        
        hashmap={}
        
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1
            else:
                hashmap[s[i]]=1
        
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]]-=1
                if hashmap[t[i]]==0:
                    del hashmap[t[i]]
            else:
                return False
    
        if len(hashmap)==0:
            return True
        else:
            return False