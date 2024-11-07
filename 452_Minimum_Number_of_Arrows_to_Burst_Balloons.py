class Solution:
    def recursiveSearch(arr: List[List[int]], cursor: int = 0) -> int:
        if cursor == len(arr) - 1:
            return 1
        else:
            nMin = arr[cursor][0]
            nMax = arr[cursor][1]
            while cursor != len(arr) - 1:
                nMin = max(nMin, arr[cursor + 1][0])
                nMax = min(nMax, arr[cursor + 1][1])  
                cursor += 1
                if nMax < nMin: return Solution.recursiveSearch(arr, cursor) + 1
            return 1              

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return Solution.recursiveSearch(sorted(points))
        
