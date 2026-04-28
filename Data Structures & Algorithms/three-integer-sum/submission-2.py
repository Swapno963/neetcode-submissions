class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        f_set = set()
        nums.sort()
        # print(nums)
        for i in range(0, len(nums)):
            j, k =  i + 1, len(nums) - 1

            while(j < k):
                # print(i,j,k)
                st = f"{nums[i]}{nums[j]}{nums[k]}"
                if st not in f_set:
                    if nums[i] + nums[j] + nums[k] == 0:
                        output.append([nums[i], nums[j], nums[k]])
                        f_set.add(st)
                        j += 1
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1

                else:
                    j += 1
                    k -= 1
        return output