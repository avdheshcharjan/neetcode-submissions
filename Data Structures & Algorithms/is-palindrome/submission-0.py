class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pal=list(s) this would not work coz of capital/small letters with ?,$, etc
        pal=[char.lower() for char in s if char.isalnum()]
        l,r=0, len(pal)-1

        while r>l:
            if pal[l]!=pal[r]:
                return False
            l+=1
            r-=1
        return True