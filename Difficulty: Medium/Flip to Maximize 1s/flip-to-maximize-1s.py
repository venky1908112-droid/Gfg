class Solution:
    def maxOnes(self, a):
        n = len(a)
        total_ones = sum(a)
        s = 0
        m_s = 0
        for x in a:
            v = 1 if x == 0 else -1
            s = max(v + s, v)
            m_s = max(m_s, s)
        return total_ones + m_s