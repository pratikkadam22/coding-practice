# function which return reverse of a string 
def reverse(s): 
	return s[::-1] 

def isPalindrome(s):
    rev = reverse(s)
    print(rev)
    
    if (s == rev):
        return True
    return False


# Driver code 
s = "malayalam"
ans = isPalindrome(s) 

if ans == 1: 
	print("Yes") 
else: 
	print("No") 
