class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = float('inf')
        ln = len(arr)
        st, ed = 0, 0
        for i in range(ln-k+1):
            diff = 0
            r = i

            while r < i+k and r < ln:
                diff += abs(arr[r] - x)
                r += 1

            if res > diff:
                res = diff
                st = i
                ed = r
        # print(st, " - ", ed)?
        return arr[st:ed]

