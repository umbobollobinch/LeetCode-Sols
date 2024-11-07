class Solution(object):
    def minCost(self, colors, neededTime):
        tmp = ""
        i = 0
        sum = 0
        tmpsum = 0
        tmpmax = 0
        
        for elem in colors:
            #print(elem)
            if elem == tmp:
                tmpsum += neededTime[i]
                tmpmax = max(neededTime[i], tmpmax)
            else:
                sum += (tmpsum - tmpmax)
                tmpsum = neededTime[i]
                tmpmax = neededTime[i]
            tmp = elem
            i += 1
        sum += (tmpsum - tmpmax)
        return sum
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        
