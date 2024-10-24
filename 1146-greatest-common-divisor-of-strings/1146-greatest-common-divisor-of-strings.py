
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Get the GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # Candidate for the largest divisor string
        candidate = str1[:gcd_length]
        
        # Check if the candidate can form both str1 and str2
        if candidate * (len(str1) // gcd_length) == str1 and candidate * (len(str2) // gcd_length) == str2:
            return candidate
        else:
            return ""

         

        