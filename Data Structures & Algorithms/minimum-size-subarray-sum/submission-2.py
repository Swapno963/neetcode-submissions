class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ln = len(nums)
        res = ln + 10
        for i in range(ln):
            sm = 0
            r = i

            while(r < ln and sm < target):
                sm += nums[r]
                if sm >= target:
                    res = min(res, r-i + 1)
                r += 1
                
        if res > ln:
            return 0
        else:
            return res