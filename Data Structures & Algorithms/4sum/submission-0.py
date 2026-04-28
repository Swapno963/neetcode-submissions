class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        f_set = set()
        nums.sort()
        # print(nums)
        for h in range(0, len(nums)-3):
            for i in range(h+1, len(nums)-2):
                j, k =  i + 1, len(nums) - 1

                while(j < k):
                    # print(h,i,j,k)
                    st = f"{nums[h]}{nums[i]}{nums[j]}{nums[k]}"
                    if st not in f_set:
                        if nums[h] + nums[i] + nums[j] + nums[k] == target:
                            output.append([nums[h], nums[i], nums[j], nums[k]])
                            f_set.add(st)
                            j += 1
                            k -= 1
                        elif nums[h] + nums[i] + nums[j] + nums[k] > target:
                            k -= 1
                        elif nums[h] + nums[i] + nums[j] + nums[k] < target:
                            j += 1

                    else:
                        j += 1
                        k -= 1
        return output