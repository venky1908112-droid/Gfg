class Solution:
    def visibleBuildings(self, arr):
        # code here
        m = -1
        c = 0
        for x in arr:
            if x >= m:
                m = x
                c += 1
        return c
        