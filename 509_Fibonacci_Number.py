class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            n1 = 1
            n2 = 0
            for i in range(n - 2 + 1):
                n0 = n1 + n2
                n2 = n1
                n1 = n0
            return n0
        """
        :type n: int
        :rtype: int
        """
        
