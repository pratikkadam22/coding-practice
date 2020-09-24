# Find the longest subarray where:
# number of values greater than equal to 10 = number of values less than 10

def equal_ones_zeroes(input, n):
    curr_sum, maxlen, end_index = 0, 0, 0
    hashmap = {}
    for i in range(n):
        if input[i] >= 10:
            curr_sum += 1
        else:
            curr_sum -= 1
        if curr_sum == 0:
            maxlen = i + 1
            end_index = i
        if curr_sum in hashmap:
            if i - hashmap[curr_sum] > maxlen:
                maxlen = i - hashmap[curr_sum]
                end_index = i
        else:
            hashmap[curr_sum] = i
    if maxlen == len(input):
        print(input)
        return maxlen
    res = input[end_index: end_index - maxlen: -1]
    print(res[::-1])
    return maxlen
 
input = [1,5,6,10,23,14,2,5,29,2,1,12]
n = len(input)     
print(equal_ones_zeroes(input, n))