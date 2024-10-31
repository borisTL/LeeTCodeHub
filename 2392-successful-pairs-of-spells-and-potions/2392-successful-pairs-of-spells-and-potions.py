class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        size_potions = len(potions)
        size_spells  = len(spells)
        pairs = [0]*size_spells 
        potions.sort()
        for i in range(size_spells):
            lo,hi=0,size_potions-1
            while (lo<=hi):
                mid=(lo+hi)//2
                if potions[mid]*spells[i] >= success:
                    hi=mid-1
                else:
                    lo=mid+1
            pairs[i]=size_potions - lo
        return pairs
        