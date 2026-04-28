class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sm = 0
        for i in range(len(prices)-1):
            res = prices[i+1] - prices[i]
            # profits.append(res)
            if res > 0:
                sm += res
        return sm