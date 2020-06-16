import sys

# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        start_time = []
        for interval in intervals:
            start_time.append(interval.start)

        sorted_index = [i[0] for i in sorted(enumerate(start_time), key=lambda x: x[1])]

        rooms = []
        for idx in sorted_index:
            interval = intervals[idx]

            if len(rooms) == 0:
                rooms.append([interval])
                continue

            room_idx_with_minimal_waiting_time = -1
            minimal_waiting_time = sys.maxsize
            for idx in range(len(rooms)):
                last_meeting = rooms[idx][-1]
                if last_meeting.end < interval.start and interval.start - last_meeting.end < minimal_waiting_time:
                    room_idx_with_minimal_waiting_time = idx

            if room_idx_with_minimal_waiting_time >= 0:
                rooms[room_idx_with_minimal_waiting_time].append(interval)
            else:
                rooms.append([interval])

        return len(rooms)
