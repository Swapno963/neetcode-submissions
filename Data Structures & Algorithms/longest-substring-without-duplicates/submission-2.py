class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, mx = 0, 0, 0
        pre = 0
        st = set()
        while r < len(s):
            # print(mx)
            if s[r] not in st:
                st.add(s[r])
                r += 1
                mx += 1
            else:
                l += 1
                r = l
                st.clear()
                mx = 0
            pre = max(mx, pre)
        return pre