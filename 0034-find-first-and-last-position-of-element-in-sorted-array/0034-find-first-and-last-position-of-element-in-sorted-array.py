class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        l, r = 0, len(nums) - 1
        indexs, indexf = -1, -1
    
    # Find the first occurrence
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                indexs = mid
                r = mid - 1  # Narrow the search range to the left
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

    # Reset the pointers for the second search
        le, ri = 0, len(nums) - 1
    
    # Find the last occurrence
        while le <= ri:
            mid = (le + ri) // 2
            if nums[mid] == target:
                indexf = mid
                le = mid + 1  # Narrow the search range to the right
            elif nums[mid] < target:
                le = mid + 1
            else:
                ri = mid - 1

        return [indexs, indexf]