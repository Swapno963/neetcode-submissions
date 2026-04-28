class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        one_third = n // 3
        count = {}
        for num in nums:
            occur_time = count.get(num, 0)
            count[num] = occur_time + 1
            # if occur_time == 0
        res = []
        for key, value in count.items():
            if value > one_third:
                res.append(key)
        return res