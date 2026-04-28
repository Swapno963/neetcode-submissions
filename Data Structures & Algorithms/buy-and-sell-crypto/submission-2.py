class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, mx = 0, 1, 0
        while r < len(prices):
            # print(l, " ", r)
            if prices[l] < prices[r]:
                mx = max(mx, prices[r] - prices[l])

            else:
                l = r
            r += 1
        return mx