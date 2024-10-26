class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

        # Если значение в середине больше, чем значение в конце, то минимальный элемент справа
            if nums[mid] > nums[right]:
                left = mid + 1
        # Если mid <= right, минимальный элемент может быть в левой половине или на mid
            else:
                right = mid

    # Когда left == right, мы нашли минимальный элемент
        return nums[left]

        