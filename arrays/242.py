#Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        n,m = len(s), len(t)

        if n != m:
            return False
    
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True
        
