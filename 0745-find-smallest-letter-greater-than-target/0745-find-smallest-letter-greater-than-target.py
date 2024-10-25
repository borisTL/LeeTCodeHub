class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters)
        while l < r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
        return letters[r] if r < len(letters) else letters[0]