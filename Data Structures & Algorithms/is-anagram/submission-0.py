class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_s=list(s)
        char_t=list(t)
        char_s.sort()
        char_t.sort()
        for i in range(len(char_t)):
            if char_s[i] !=char_t[i]:
                return False
        return True
        
        # SIMPLER VERSION AND QUITE EFFECTIVE
        # if len(s)!=len(t):
        #     return False
        # # can directly sort and compare using
        # return sorted(s)==sorted(t)
        