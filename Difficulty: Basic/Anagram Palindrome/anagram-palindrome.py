from collections import Counter
class Solution:
    def canFormPalindrome(self, s):
        freq = Counter(s)
        odd = 0
        for key, val in freq.items():
            if val & 1:
                odd += 1
            if odd > 1:
                return False
        return True
        
                