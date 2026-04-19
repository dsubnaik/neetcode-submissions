class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashtable={}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in hashtable:
                hashtable[s[i]]+=1
            else:
                hashtable[s[i]]=1
        

        for i in range(len(t)):
            if t[i]in hashtable:
                hashtable[t[i]]-=1
            else:
                hashtable[t[i]]=1
            
            if hashtable[t[i]]==0:
                hashtable.pop(t[i])


        if len(hashtable)==0:
            return True
        else:
            return False

