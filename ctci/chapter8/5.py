# 8.5: Recursive Multiply

def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    s = smaller >> 1
    half_prod = min_product_helper(s, bigger)
    if smaller % 2 == 0:
        return half_prod + half_prod
    elif smaller % 2 == 1:
        return half_prod + half_prod + bigger

def min_product(num1, num2):
    s = min(num1, num2)
    b = max(num1, num2)
    return min_product_helper(s, b)

print(min_product(7,8))
print(min_product(17,23))
print(min_product(15,35))
print(min_product(16,35))

# Approach with Memoization:
# def min_product_helper(smaller, bigger, memo):
#     if smaller == 0:
#         return 0
#     elif smaller == 1:
#         return bigger
#     elif memo[smaller] > 0:
#         return memo[smaller]
#     s = smaller >> 1
#     n1 = min_product_helper(s, bigger, memo)
#     n2 = n1
#     if smaller % 2 == 1:
#         n2 = min_product_helper(smaller - s, bigger, memo)
#     memo[smaller] = n1 + n2
#     return memo[smaller]

# def min_product(num1, num2):
#     s = min(num1, num2)
#     b = max(num1, num2)
#     memo = [0] * (s + 1)
#     return min_product_helper(s, b, memo)