class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        size=len(candies)
        biggest=max(candies)
        boolarray=[(candies[i]+extraCandies>=biggest)for i in range(size)]
        return boolarray
        