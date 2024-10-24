class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        snowBallse=0
        size=len(nums)
        for idx in range(size):
            if nums[idx] == 0:
                snowBallse+=1
            elif(snowBallse > 0):
                t=nums[idx]
                nums[idx]=0
                nums[idx-snowBallse]=t

        