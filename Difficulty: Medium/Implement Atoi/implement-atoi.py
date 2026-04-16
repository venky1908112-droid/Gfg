class Solution:
    def myAtoi(self, s):
        s = ''.join(s.split())
        n = len(s)
        sign = 1
        start_idx = 0
        if s[0] == '-':
            sign = -1
            start_idx = 1
        if s[0] == '+':
            start_idx = 1
        end_idx = start_idx
        while end_idx < n and s[end_idx].isdigit():
            end_idx += 1
        num = int(s[start_idx : end_idx]) * sign
        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648
        return num