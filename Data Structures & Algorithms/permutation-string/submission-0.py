class Solution:
    def get_count(self, s):
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
        return count

    def checkInclusion(self, s1: str, s2: str) -> bool: 
        count = self.get_count(s1)
        l = 0
        r = len(s1)
        while r <= len(s2):
            new_char = s2[l:r]
            new_count = self.get_count(new_char)
            l += 1
            r += 1
            if count == new_count:
                return True
        return False