def isOperand(c) :  
  
    # If the character is a digit then it must  
    # be an operand  
    return c.isdigit();  
  
def evaluatePrefix(exprsn) :  
  
    Stack = [];  
  
    for j in range(len(exprsn) - 1, -1, -1) :  
  
        # push operand to Stack  
        # To convert exprsn[j] to digit subtract  
        # '0' from exprsn[j].  
        if (isOperand(exprsn[j])) : 
            Stack.append(int(exprsn[j]));  
  
        else : 
  
            # Operator encountered  
            # Pop two elements from Stack  
            o1 = Stack[-1]; 
            Stack.pop(); 
            o2 = Stack[-1]; 
            Stack.pop(); 
              
            # Use switch case to operate on o1 
            # and o2 and perform o1 O o2. 
            if (exprsn[j] == '+') : 
                Stack.append(o1 + o2); 
                  
            elif (exprsn[j] == '-') : 
                Stack.append(o1 - o2); 
                  
            elif (exprsn[j] =='*') : 
                Stack.append(o1 * o2); 
                  
            elif (exprsn[j] =='/') : 
                Stack.append(o1 / o2); 
                  
    return Stack[-1];  
  
# Driver code  
if __name__ == "__main__" :  
  
    exprsn = "+ 9 * 3 + 101 199"
    stack = []
    for j in range(0, len(exprsn)):
        i = j
        if exprsn[i]!= " ":
            x = ""
            while i < len(exprsn) and exprsn[i] != " ":
                x = x + exprsn[i]
                i = i + 1
            stack.append(x)
        j = i
    print(stack)
    #print(evaluatePrefix(stack))  