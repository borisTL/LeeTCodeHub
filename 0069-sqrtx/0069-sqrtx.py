class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo,hi=0,x
        res=0
        while lo <= hi:
            mid = (lo + hi)//2

            if mid * mid == x:
                return mid 

            elif mid*mid > x:
                res=mid
                hi = mid -1
            else:
                lo = mid +1
        return res - 1 
        