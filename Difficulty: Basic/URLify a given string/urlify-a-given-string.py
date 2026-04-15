class Solution:
    def URLify(self, s): 
        # code here
        return '%20'.join(s.split(" "))