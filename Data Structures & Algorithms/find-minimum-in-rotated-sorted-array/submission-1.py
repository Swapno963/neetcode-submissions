class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        mn = nums[0]
        while l <= r:
            mid = (l + r) // 2
            mn = min(mn, nums[mid])
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1

                

            # print(l, " ", r, "mid :", mid)
        return mn