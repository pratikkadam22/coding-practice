# 8.3: Magic Index

def magic(arr, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return magic(arr, mid + 1, end)
    elif arr[mid] > mid:
        return magic(arr, start, mid - 1)

def magic_distinct(arr, start, end):
    if end < start:
        return -1
    midIndex = (start + end) // 2
    if arr[midIndex] == midIndex:
        return midIndex
    
    left = magic_distinct(arr, start, min(midIndex - 1, arr[midIndex]))
    if left >= 0:
        return left
    
    right = magic_distinct(arr, max(midIndex + 1, arr[midIndex]), end)
    return right

arr1 = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
arr2 = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]

print(magic(arr1, 0, len(arr1) - 1))
print(magic_distinct(arr2, 0, len(arr2) - 1))