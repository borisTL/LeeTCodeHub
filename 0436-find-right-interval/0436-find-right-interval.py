class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        sorted_starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result = []
        index = -1
        for i in range(len(intervals)):
            target = intervals[i][-1]
            
            l , r = 0 ,len(sorted_starts )
            while l < r:
                mid = (l +r) // 2
                if sorted_starts [mid][0] >= target:
                   
                    index = sorted_starts[mid][-1] 
              
                    r = mid  
                else:
                    l = mid +1
            result.append(index if index != -1 else -1 )
            index = -1
           
        return result
