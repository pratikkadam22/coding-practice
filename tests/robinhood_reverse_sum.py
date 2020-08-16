# Given an array of non-negative integers arr, your task is to count the number
# of pairs (i,j) such that i<=j and
# arr[i] + rev(arr[j]) = arr[j] + rev(arr[i])
# Not: rev(int) is a function which reverses the number (eg. 24 -> 42, 20 -> 2)

def oppositeSums(arr):
    def rev(num):
        res = 0
        while num > 0:
            res = (res * 10) + (num % 10)
            num = num // 10
        return res

    n = len(arr)
    sums, sumCount = [], {}
    result = 0
    for i in range(n):
        t = arr[i] - rev(arr[i])
        sums.append(t)
        sumCount[t] = sumCount.get(t, 0) + 1
    print(sumCount)
    for d in sumCount:
        val = sumCount[d]
        if val > 1:
            result += (val*(val+1)) // 2
        else:
            result += 1
    return result

test1 = [1, 20, 2, 11]
answer = oppositeSums(test1)
print(answer)