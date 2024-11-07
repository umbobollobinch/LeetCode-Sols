class Solution(object):
    def shipWithinDays(self, weights, days):
        vmin = 0
        vmax = sum(weights)

        while vmax >= vmin:
            mid = (vmax + vmin + 1) // 2

            cnt = 1
            tmp = 0
            i = 0
            while cnt <= days:
                if tmp > mid:
                    tmp = weights[i - 1]
                    cnt += 1
                else:
                    if i == len(weights):
                        vmax = mid - 1
                        break
                    tmp += weights[i]
                    i += 1
            else:
                vmin = mid + 1

        return((vmax + vmin) // 2 + 1)
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
