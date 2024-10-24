
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        list1=[]
        counter=1
        size=len(chars)
        for i in range (size):
            if i+1<size and chars[i]==chars[i+1] :
                counter+=1
            else:
                if counter>1:
                    list1.append(chars[i])
                    list1.extend(list(str(counter)))
                else:
                    list1.append(chars[i])

                
                counter=1
        chars[:] = list1
        return len(list1)

      
        