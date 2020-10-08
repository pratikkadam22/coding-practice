# 8.13: Stack of Boxes
# Complexity: O(n!) (maybe)

def createStack(boxes):
    boxes.sort(key = lambda x: -x[0])
    memo = [0] * len(boxes)
    max_height = 0
    for i in range(len(boxes)):
        height = helper(boxes, i, memo)
        max_height = max(max_height, height)
    return max_height

def helper(boxes, bottom_index, memo):
    if bottom_index < len(boxes) and memo[bottom_index] > 0:
        return memo[bottom_index]
    prev_w, prev_h, prev_d = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index + 1, len(boxes)):
        w, h, d = boxes[i]
        if prev_w > w and prev_h > h and prev_d > d:
            height = helper(boxes, i, memo)
            max_height = max(height, max_height)
    max_height += prev_h
    memo[bottom_index] = max_height
    return max_height

boxes = [(1,1,1),(2,2,2),(3,3,3),(1,1,1)]
print(createStack(boxes))