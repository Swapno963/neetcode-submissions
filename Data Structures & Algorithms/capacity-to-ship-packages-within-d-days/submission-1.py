class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        mx = max(weights)
        rs = r

        def days_needed(cap):
            ships, curCap = 1, cap
            for w in weights:
                if curCap - w < 0:
                    ships += 1 
                    curCap = cap
                curCap -= w
            return ships
        while l <= r:
            mid = (l + r) // 2
            
            ships = days_needed(mid)
            # print("ships : ", ships, ", mid : ", mid)
            if ships > days:
                l = mid + 1
            else: 
                r =  mid -1
                rs = min(rs, mid)
        return rs