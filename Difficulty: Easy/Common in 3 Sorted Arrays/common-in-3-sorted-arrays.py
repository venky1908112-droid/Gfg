class Solution:
    def commonElements(self, a, b, c):
        # code here
        i = 0
        j = 0
        k = 0
        res = []
        while i < len(a) and j < len(b) and k < len(c):
            x, y, z = a[i], b[j], c[k]
            if x == y == z:
                if not res or res[-1] != x:
                    res.append(x)
                i += 1
                j += 1
                k += 1
            else:
                m = min(x, y, z)
                if m == x:
                    i += 1
                elif m == y:
                    j += 1
                else:
                    k += 1
        return res