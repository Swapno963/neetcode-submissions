class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print(nums)
        # return 0
        num_frequency = {}
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1
        
        sorted_by_frequency = sorted(num_frequency.items(), key=lambda x :x[1], reverse=True)
        # print(sorted_by_frequency)
        # for key, value in num_frequency.items():
        #     print(f"{key}: {value}")
        items = []
        for i in range(k):
            items.append(sorted_by_frequency[i][0])
        print(items)
        return items