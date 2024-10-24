class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
    
        size1=len(word1)
        size2=len(word2)

        word3=''
        min_size=min(size1,size2)

        for i in range(min_size):
            word3+=word1[i]+word2[i]
            
        word3 += word1[min_size:] + word2[min_size:]
        return word3
        