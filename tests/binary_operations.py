# CodeSignal Question
# Input = (n: int, operations: List[str])
# n = the size of binary string of zeroes. eg. if n = 3, string = '000'
# operations = it can contain 'L' and 'C{index}' 
#             'L' = which means find earliest 0 in string and make it 1. If no zero, do nothing.
#             'C{index}' = for eg. 'C2' means make value at 2nd index to '0'.
def binary_operations(n, operations):
    arr = ''
    for i in range(n):
        arr += '0'
    for o in operations:
        if o == 'L':
            ind = arr.index('0') if '0' in arr else None
            if ind is not None:
                arr = arr[:ind] + '1' + arr[ind+1:]
        else:
            ind = int(o[1])
            arr = arr[:ind] + '0' + arr[ind+1:]
    return arr

n = 8
operations = ['L','L','C5','C0']
res = binary_operations(n, operations)
print(res)
             

