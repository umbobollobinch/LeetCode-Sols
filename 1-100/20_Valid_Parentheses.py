class Solution(object):
    def isValid(self, s):
        dic = {")": "(", "}": "{", "]": "["}
        list = []
        
        for char in s:
            if char in dic.values():
                list.append(char)
            else:
                if len(list) < 1:
                    return False
                else:
                    if dic[char] == list[-1]:
                        del list[-1]
                    else:
                        return False
        if len(list) == 0: 
            return True 
        else: return False
        
        """
        :type s: str
        :rtype: bool
        """
