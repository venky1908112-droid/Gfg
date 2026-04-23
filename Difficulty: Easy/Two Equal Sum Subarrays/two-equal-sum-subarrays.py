class Solution:
    def canSplit(self, arr):
        #code here
        prefix_sum = 0
        total_sum = sum(arr)
        for x in arr:
            prefix_sum += x
            if total_sum - prefix_sum == prefix_sum:
                return True
        return False