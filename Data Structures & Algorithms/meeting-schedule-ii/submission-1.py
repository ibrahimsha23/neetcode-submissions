"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        max_meeting_rooms = 0

        events = []

        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        events.sort(key=lambda x: (x[0], x[1]))

        meeting_counter = 0
        for event in events:
            meeting_counter += event[1]
            max_meeting_rooms = max(max_meeting_rooms, meeting_counter)
        return max_meeting_rooms



        