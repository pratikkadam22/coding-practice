def isOperand(c) :  
  
    # If the character is a digit then it must  
    # be an operand  
    return c.isdigit();  
  
def evaluatePostfix(exprsn) :  
  
    Stack = [];  
  
    for j in range(0, len(exprsn)) :  
  
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
                Stack.append(o2 + o1); 
                  
            elif (exprsn[j] == '-') : 
                Stack.append(o2 - o1); 
                  
            elif (exprsn[j] =='*') : 
                Stack.append(o2 * o1); 
                  
            elif (exprsn[j] =='/') : 
                Stack.append(o2 / o1); 
                  
    return Stack[0];  
  
# Driver code  
if __name__ == "__main__" :  
  
    exprsn = "210+96-/";  
    print(evaluatePostfix(exprsn));  