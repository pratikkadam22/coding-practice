# 252. Meeting Rooms II

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (s < e), find the minimum
# number of conference rooms required.
# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1

import heapq

def meeting_rooms(timings):
    if timings is None or len(timings) == 0:
        return 0
    timings.sort(key = lambda x: x[0])
    heap = []
    heapq.heapify(heap)
    for i in timings:
        i[0], i[1] = i[1], i[0]
    
    heapq.heappush(heap, timings[0])
    for i in range(1, len(timings)):
        earliest = heapq.heappop(heap)
        current = timings[i]
        if current[1] >= earliest[0]:
            earliest[0] = current[0]
        else:
            heapq.heappush(heap, current)
        heapq.heappush(heap, earliest)
    return len(heap)

input1 = [[0,30],[15,20],[5,10]]
print(meeting_rooms(input1))

input2 = [[7,10],[2,4]]
print(meeting_rooms(input2))