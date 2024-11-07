class Solution(object):
    def lengthOfLastWord(self, s):
        result = s.split()[len(s.split()) - 2] if s.split()[len(s.split()) - 1] == "" else  s.split()[len(s.split()) - 1]
        return(len(result))
