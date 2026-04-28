class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        new_word = ""
        mxi = 0

        for i in range(min(n, m)):
            new_word += word1[i] + word2[i]
            mxi = i
        if n - 1 > mxi:
            new_word += word1[mxi + 1 : n]
        if m - 1 > mxi:
            new_word += word2[mxi + 1 : m]
        
        return new_word