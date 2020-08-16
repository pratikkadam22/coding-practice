# AMAZON ONLINE TEST - ADYA PANDEY
# Find the sets of foreground and background application pairs that optimally utilize
# the given device for a given list of foreground and a given list of background applications.

import sys

def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    if deviceCapacity == 0 or len(foregroundAppList) == 0 or len(backgroundAppList) == 0:
        return []
    foregroundAppList.sort(key = lambda x: x[1])
    backgroundAppList.sort(key = lambda x: x[1])

    i = 0
    j = len(backgroundAppList) - 1
    maxutil = 0
    while(i < len(foregroundAppList) and j >= 0):
        a = foregroundAppList[i][1]
        b = backgroundAppList[j][1]
        if (a + b) <= deviceCapacity:
            maxutil = max(a+b, maxutil)
            i += 1
        else:
            j -= 1
    result = []
    temp = {}

    for f in foregroundAppList:
        if f[1] not in temp:
            temp[f[1]] = []
        temp[f[1]].append(f[0])
    
    for b in backgroundAppList:
        if maxutil - b[1] in temp:
            for x in temp[maxutil - b[1]]:
                result.append([x, b[0]])

    return result

deviceCapacity = 10
foregroundAppList = [[1,3],[2,5],[3,7],[4,10]]
backgroundAppList = [[1,2],[2,3],[3,4],[4,5]]
print(optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList))