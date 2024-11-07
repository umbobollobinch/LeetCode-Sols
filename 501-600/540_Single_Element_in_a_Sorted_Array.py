class Solution(object):
    def singleNonDuplicate(self, nums):
        l = len(nums) - 1
        m = l // 2
        n = m
        if l == 0: return nums[0]

        while n > 0:
            if (nums[m-1] != nums[m]) and (nums[m + 1] != nums[m]): return nums[m]

            n //= 2 
            cond1 = (nums[m] == nums[m + 1]) and ((l - m) % 2 == 1)
            cond2 = (nums[m] != nums[m + 1]) and ((l - m) % 2 == 0)
            m -= n if (cond1 or cond2) else -n
        
        return nums[0] if (cond1 or cond2) else nums[l]
        """
        :type nums: List[int]
        :rtype: int
        """
