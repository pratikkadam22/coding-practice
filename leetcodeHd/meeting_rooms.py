# 252. Meeting Rooms

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (s < e), determine
# if a person could attend all the meetings.

# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: False

# Example 2:
# Input: [[7,10],[2,4]]
# Output: True

def meeting_rooms(timings):
    timings.sort(key = lambda x: x[0])
    for i in range(len(timings)-1):
        if timings[i][1] > timings[i+1][0]:
            return False
    return True

input1 = [[0,30],[15,20],[5,10]]
print(meeting_rooms(input1))

input2 = [[7,10],[2,4]]
print(meeting_rooms(input2))