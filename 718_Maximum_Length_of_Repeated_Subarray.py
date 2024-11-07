class Solution(object):
    def findLength(self, nums1, nums2):
        ans = 0
        tmparr = [[0] * (len(nums2) + 1) for i in range(2)]
        
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums2[j] == nums1[i]:
                    tmparr[1][j] = tmparr[0][j + 1] + 1
                else:
                    tmparr[1][j] = 0
            ans = max([max(tmparr[1][:]), ans])    
            tmparr[0][:] = tmparr[1][:]
        return(ans)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
