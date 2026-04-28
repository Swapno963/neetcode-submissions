
class Solution:
    def check_palindrome(self,s,le,ri)-> bool:  
    # print(le, ri)  
        while(le<ri):
            if s[le] != s[ri]:
                return False
            le += 1
            ri -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        s.lower()
        # Check is it palindrome or not
        l,r = 0, len(s)-1       
        while(l<r):
            if s[l] != s[r]:
                r_l = self.check_palindrome(s, l+1, r)
                r_r = self.check_palindrome(s,l, r-1)
                return r_l or r_r
            l += 1
            r -= 1
        return True