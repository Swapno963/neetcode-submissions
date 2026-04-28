class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dc = {}
        mx = 0
        is_first_pos = True
        for item in nums:
            if item >= 0 and is_first_pos:
                mx = item
                is_first_pos = False
                
            if item >= 0:
                dc[item] = True
                if mx < item:
                    mx = item
        for i in range(1, mx):
            present = dc.get(i,False)
            # print(present)
            if not present:
                return i
        return mx + 1