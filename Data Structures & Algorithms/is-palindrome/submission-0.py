class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to plane string
        new_s = ""
        s.replace(" ", "")
        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()
                
        # Check is it palindrome or not
        l,r = 0, len(new_s)-1
        is_palindrome = True
        while(l<r):
            if new_s[l] != new_s[r]:
                is_palindrome = False
                break
            l += 1
            r -= 1
        return is_palindrome