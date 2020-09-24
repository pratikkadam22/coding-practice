# Find the longest subarray where:
# number of values greater than equal to 10 > number of values less than 10

def more_ones(input, n):
    curr_sum, maxlen, end_index = 0, 0, 0
    hashmap = {}
    for i in range(n):
        if input[i] >= 10:
            curr_sum += 1
        else:
            curr_sum -= 1
        if curr_sum >= 1:
            maxlen = i + 1
            end_index = i
        elif curr_sum not in hashmap:
            hashmap[curr_sum] = i
        if (curr_sum - 1) in hashmap:
            if i - hashmap[curr_sum - 1] > maxlen:
                maxlen = i - hashmap[curr_sum - 1]
                end_index = i
    print("End Index:", end_index)
    if end_index - maxlen < 0:
        print(input[:end_index + 1])
        return maxlen
    res = input[end_index: end_index - maxlen: -1]
    print(res[::-1])
    return maxlen
 
# input = [5,6,10,23,14,2,5,29,2,11]
# input = [1,5,6,10,23]
input = [4, 5,11, 7,12,13, 3, 18,15, 5, 2, 1]

print("Input array length:", len(input))
n = len(input)     
print("Result array length:", more_ones(input, n))