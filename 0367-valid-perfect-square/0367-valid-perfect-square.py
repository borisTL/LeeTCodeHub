class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num  # Start r at num instead of num - 1
        while l <= r:
            mid = (l + r) // 2
            target = mid * mid
            if target == num:
                return True
            if target < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

        