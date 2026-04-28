class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        mn = nums[0]        
        mx = nums[0]
        dc = {}
        for num in nums:
            dc[num] = True
            if num < mn:
                mn = num
            if num > mx:
                mx = num
        occured = 1
        tem = 1
        for num in range(mn, mx+1):
            have =dc.get(num+1, False) 
            if have:
                tem += 1
                if tem > occured:
                    occured = tem

            else:
                tem = 0

        return occured
        # print(f"The min is : {mn}, and the max is {mx} and dict is {dc},occured {occured}", )