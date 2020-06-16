
def test_case1():
    test_data = [(0, 30), (5, 10), (15, 20)]
    intervals = []
    for interval_data in test_data:
        interval = Interval(interval_data[0], interval_data[1])
        intervals.append(interval)

    solution = Solution()
    ans = solution.minMeetingRooms(intervals)
    assert ans == 2


def test_case2():
    test_data = [(65,424),(351,507),(314,807),(387,722),(19,797),(259,722),(165,221),(136,897)]


if __name__ == '__main__':

    test_case1()