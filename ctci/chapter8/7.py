# 8.7: Permutations without Dups

def helper(prefix, remainder, results):
    if len(remainder) == 0:
        results.append(prefix)

    for i in range(len(remainder)):
        before = remainder[:i]
        after = remainder[i + 1:]
        c = remainder[i]
        helper(prefix + c, before + after, results)

def get_perms(string):
    results = []
    helper("", string, results)
    return results

print(get_perms("abcd"))
print(get_perms("abcde"))
print(get_perms("abc"))
print(get_perms("ab"))