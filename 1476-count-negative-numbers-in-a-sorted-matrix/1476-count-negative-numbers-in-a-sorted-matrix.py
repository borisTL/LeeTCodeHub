class Solution(object):

    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
     
        row, col = len(grid) - 1, 0
    

    # Traverse until we are out of bounds
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                # All elements to the right are also negative
                count += len(grid[0]) - col
                row -= 1  # Move up to the previous row
            else:
                col += 1  # Move right in the same row
        return count 
            
