# Python program to find sum of array 
# elements using recursion. 

# Return sum of elements in A[0..N-1] 
# using recursion. 
def _findSum(arr, N):
    if len(arr)== 1:
        return arr[N-1]
    else:
        return arr[N-1]+_findSum(arr[:N-1], N-1)

arr = [] 
# input values to list 
arr = [1, 2, 3, 4, 5] 

# calculating length of array 
N = len(arr) 

ans =_findSum(arr,N) 
print (ans) 

# This code is contributed by Khare Ishita 
