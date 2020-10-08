# 8.14: Boolean Evaluation
# The Catalan numbers method (mentioned at the end of this question's solution in CTCI) is not used here. 
# Complexity: O(n!) (maybe)

def count_eval(s, result, memo):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1 if string_to_bool(s) == result else 0
    k = s + "," + str(result)
    if k in memo:
        return memo[k]
    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left, right = s[:i], s[i+1:]
        left_true = count_eval(left, True, memo)
        left_false = count_eval(left, False, memo)
        right_true = count_eval(right, True, memo)
        right_false = count_eval(right, False, memo)
        total = (left_true + left_false) * (right_false + right_true)
        total_true = 0
        if c == "^":
            total_true = (left_true * right_false) + (left_false * right_true)
        elif c == "&":
            total_true = left_true * right_true
        elif c == "|":
            total_true = (left_true * right_true) + (left_false * right_true) + (left_true * right_false)
        sub_ways = total_true if result else total - total_true
        ways += sub_ways
    memo[k] = ways
    return ways

def string_to_bool(s):
    return True if s == "1" else False

memo = {}
# print(count_eval("1", True, memo)) # 1
# print(count_eval("0", True, memo)) # 0
# print(count_eval("0", False, memo)) # 1
# print(count_eval("1&1", True, memo)) # 1
# print(count_eval("1|0", False, memo)) # 0
# print(count_eval("1^0", True, memo)) # 1
# print(count_eval("1&0&1", True, memo)) # 0
# print(count_eval("1|1^0", True, memo)) # 2
# print(count_eval("1^0|0|1", False, memo)) # 2
# print(count_eval("1^0|0|1", True, memo)) # 3
print(count_eval("0&0&0&1^1|0", True, memo)) # 10