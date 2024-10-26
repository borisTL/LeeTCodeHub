class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        #[snap]
        self.data = arr = [[(0, 0)] for i in range(length)]
        self.snap_id = 0

        

    def set(self, index, val):
        """
        Устанавливает значение val для элемента на позиции index для текущего snap_id
        """
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")

        
        if self.data[index][-1][0] == self.snap_id:
            
            self.data[index][-1] = (self.snap_id, val)
        else:
        
            self.data[index].append((self.snap_id, val))
        

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id +=1 
        return self.snap_id -1

    def get(self, index, snap_id):
        """
     
        """
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")

       
        values = self.data[index]
        left, right = 0, len(values) - 1
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= snap_id:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)