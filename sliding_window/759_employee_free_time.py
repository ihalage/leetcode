class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"
    
class Solution:
    """
    We DO NOT want to treat each employee individually.
    First create a single list of all meeting times of all employees and then sort it by the meeting starting time
    compare the end value of the previous interval against the start value of the current interval
    if start value of current interval is larger, then there is free time
    end time of the previous interval is updated as max(prevEnd, curEnd)
    """
    def employee_free_time(self, schedule):
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])
        intervals.sort(key=lambda x: x[0])
        
        result = []
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            curStart = intervals[i][0]
            curEnd = intervals[i][1]
            if prevEnd<curStart: # we have some free time
                result.append(Interval(prevEnd, curStart))
            prevEnd = max(prevEnd, curEnd)

        return result