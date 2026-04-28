class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 1
        nums = []
        for i in range(len(numbers) - 1):
            j = i + 1
            while j < len(numbers):
                if numbers[i] + numbers[j] == target:
                    nums.append(i + 1)
                    nums.append(j + 1)
                    return nums

                else:
                    j += 1      