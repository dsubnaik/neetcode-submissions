class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = Counter(s1)
        s2_count = {}
        left = 0
        
        for r in range(len(s2)):
            
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            
            if r - left + 1 > len(s1):
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left += 1
            
            if s1_count == s2_count:
                return True
        
        return False