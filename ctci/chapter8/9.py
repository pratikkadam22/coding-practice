# 8.9: Parens

def generate_parens(n):
    res = []
    helper("", 0, 0, res, n)
    return res

def helper(s, open, close, res, n):
    if len(s) == n * 2:
        res.append(s)
    if open < n:
        helper(s + "(", open + 1, close, res, n)
    if close < open:
        helper(s + ")", open, close + 1, res, n)

n = 4
ans = generate_parens(n)
print(ans)