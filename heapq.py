import heapq 

# initializing list 
li = [[0,30],[15,20],[5,10]]

# using heapify to convert list into heap 
heapq.heapify(li) 

# printing created heap 
print ("The created heap is : ",end="") 
print (list(li)) 

# using heappush() to push elements into heap 
# pushes 4 
heapq.heappush(li,[7,10]) 

# printing modified heap 
print ("The modified heap after push is : ",end="") 
print (list(li)) 

# using heappop() to pop smallest element 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(li)) 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(li)) 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(li)) 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(li)) 
