class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=1
        size=len(nums)
        zero_flag=0
        for num in nums:
            if num!=0:
                k*=num
            else:
                zero_flag+=1

        
            

        for i in range(size):

            if  nums[i]!=0 and zero_flag==0:
                nums[i]= k // nums[i]
            elif zero_flag==1 and nums[i]==0:
                nums[i]=k
            else:
                nums[i]=0
            



        return nums
        