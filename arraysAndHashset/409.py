import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = collections.Counter(s) 
        longest = 0 
        oddCenter = False

        for count in counts.values():
            longest += ( count // 2 ) * 2
            if count % 2 == 1:
                oddCenter = True  
        
        if  oddCenter:
            longest += 1 
        return longest 

