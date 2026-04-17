from collections import Counter
class Solution:
    def canFormPalindrome(self, s):
        freq = Counter(s)
        even = 0
        for key,val in freq.items():
            if not val & 1:
                even += 1
        n = len(freq)
        if n == even or n - 1 == even:
            return True
        return False