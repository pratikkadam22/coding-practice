
def printJobScheduling(arr): 
  
    # length of array 
    n, profit = len(arr), 0
  
    # Sort all jobs according to decreasing order of profit 
    arr.sort(key = lambda x: x[2], reverse=True)

    # To keep track of free time slots 
    result = [False] * n 
  
    # To store result (Sequence of jobs) 
    job = ['-1'] * n 
    
    # Iterate through all given jobs 
    for i in range(n): 
  
        # the last possible slot where job can be placed 
        last_possible_slot = min(n - 1, arr[i][1] - 1)

        for j in range(last_possible_slot, -1, -1): 
            # If a free slot is found, fill it in
            if not result[j]: 
                result[j] = True
                job[j] = arr[i][0] 
                profit += arr[i][2]
                break

    ans = [x for x in job if x != '-1']
    return ans, profit
  
# Driver Code 
# arr = [['a', 2, 100],
#        ['b', 1, 19], 
#        ['c', 2, 27], 
#        ['d', 1, 25], 
#        ['e', 3, 15]] 

# arr = [['a', 4, 20], 
#        ['b', 1, 10], 
#        ['c', 1, 40], 
#        ['d', 1, 30]] 

# arr = [['a', 1, 10], 
#        ['b', 2, 15], 
#        ['c', 3, 5], 
#        ['d', 2, 20],
#        ['e', 3, 1]] 

arr = [[1, 9, 15], 
       [3, 5, 18], 
       [5, 4, 25], 
       [7, 5, 8],
       [9, 4, 12],
       [2, 2, 2],
       [4, 7, 1],
       [6, 2, 20],
       [8, 7, 10],
       [10, 3, 5]]

jobs, profit = printJobScheduling(arr)
print("The following sequence of jobs would maximize the total profit:", jobs)
print("Maximum profit:", profit) 