class Solution:
    def myAtoi(self, s):
        # code here
        s = ''.join(s.split())
        n = len(s)
        start_idx = 0
        s_pos = 1
        if s[0] == '-':
            s_pos = -1
            start_idx = 1
        if s[0] == '+':
            start_idx = 1
        start = start_idx
        while start_idx < n and s[start_idx].isdigit():
            start_idx += 1
        num = int(s[start : start_idx]) * s_pos
        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648
        return num
            