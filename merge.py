class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals)
        L = len(intervals)
        i = 0
        while i+1 < L:
            if intervals[i+1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                print(intervals[i][1])
                intervals.pop(i+1)
                L -= 1
            else:
                i += 1
        return intervals



print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
