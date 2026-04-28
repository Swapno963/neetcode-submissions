class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            res = mid * mid
            if res == x:
                return mid
            elif res > x:
                right = mid - 1
            else:
                left = mid + 1

        if left * left < x:
            return left
        else:
            return left -1