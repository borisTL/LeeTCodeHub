class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
        # Missing count until arr[mid]
            missing_count = arr[mid] - (mid + 1)

            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1

        
        

        return left + k

             
        