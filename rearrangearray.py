def rearrange(arr, n): 
    # The following few lines are similar to partition process 
    # of QuickSort.  The idea is to consider 0 as pivot and 
    # divide the array around it. 
    i = -1
    for j in range(n): 
        if (arr[j] < 0): 
            i += 1
            # swapping of arr 
            arr[i], arr[j] = arr[j], arr[i] 
   
    # Now all positive numbers are at end and negative numbers 
    # at the beginning of array. Initialize indexes for starting 
    # point of positive and negative numbers to be swapped 
    pos, neg = i+1, 0
   
    # Increment the negative index by 2 and positive index by 1, 
    # i.e., swap every alternate negative number with next  
    # positive number 
    while (pos < n and neg < pos and arr[neg] < 0): 
  
        # swapping of arr 
        arr[neg], arr[pos] = arr[pos], arr[neg] 
        pos += 1
        neg += 2
  
# A utility function to print an array 
def printArray(arr, n): 
      
    for i in range(n): 
        print(arr[i], end=' ') 
   
# Driver program to test above functions 
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9] 
n = len(arr) 
rearrange(arr, n) 
printArray(arr, n) 