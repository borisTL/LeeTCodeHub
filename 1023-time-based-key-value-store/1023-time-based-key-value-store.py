class TimeMap(object):

    def __init__(self):
        self.data = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.data:
            self.data[key] = []

        self.data[key].append([timestamp, value])

        
        
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.data:
            return ''
        
        values = self.data.get(key , [])

        l , r = 0 ,  len(values) -1
        result = ''

        while l <= r :
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                result= values[mid][1]
                l = mid + 1
            else:
                r = mid -1 

        return result 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)